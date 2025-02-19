from ninja import Router
from .schemas import StudentsSchema, ProgressStudentSchema, ClassHeldSchema
from .models import Students, ClassesHeld
from ninja.errors import HttpError
from typing import List
from .graduacao import *
from datetime import date
treino_router = Router()

@treino_router.post("/", response={200: StudentsSchema})
def create_student(request, student_schema: StudentsSchema):
    name = student_schema.dict()['name']
    email = student_schema.dict()['email']
    belt = student_schema.dict()['belt']
    birthdate = student_schema.dict()['birthdate']

    if Students.objects.filter(email=email).exists():
        raise HttpError(400, "E-mail já cadastrado.")
    
    student = Students(
        name=name,
        email=email,
        belt=belt, 
        birthdate=birthdate
    )
    student.save()

    return student

@treino_router.get("/students/", response=List[StudentsSchema])
def list_students(request):
    students = Students.objects.all()
    
    return students

@treino_router.get("/progress_student/", response={200: ProgressStudentSchema})
def progress_student(request, student_email: str):
    student = Students.objects.get(email=student_email)
    
    current_belt = student.get_belt_display()
    
    n = order_belt.get(current_belt, 0)
    
    total_classes_next_belt = calculate_lessons_to_upgrade(n)
    total_classes_held_belt = ClassesHeld.objects.filter(student=student, current_belt=student.belt).count()
    
    missing_classes = total_classes_next_belt - total_classes_held_belt
    
    return {
        "email": student.email,
        "name": student.name,
        "belt": current_belt,
        "total_class": total_classes_held_belt,
        "classes_required_for_next_belt": missing_classes      
    }
    
    
@treino_router.post("/aula_realizada/", response={200: str})
def class_held(request, class_held: ClassHeldSchema):
    qtd = class_held.dict()['qtd']
    student_email = class_held.dict()['student_email']
    
    if qtd <= 0:
        raise HttpError(400, "Quantidade de aulas devem ser maiores que zero")
    
    student = Students.objects.get(email=student_email)
    
    for _ in range(0, qtd):
        classes_held = ClassesHeld(
            student=student,
            current_belt=student.belt
        )
        classes_held.save()
    
    return 200, f"Aula marcadaa como realizada para o aluno {student.name}"

@treino_router.put("/alunos/{student_id}")
def update_student(request, student_id: int, student_data: StudentsSchema):
    student = Students.objects.get(id=student_id)    
    
    age = date.today() - student.birthdate
    
    if int(age.days/365) < 18 and student_data.dict()['belt'] in ('A', 'R', 'M', 'P'):
        raise HttpError(400, "O aluno é menor de idade e não pode ser graduado para essa faixa.")
    
    for attr, value in student_data.dict().items():
        if value:
            setattr(student, attr, value)
            
    student.save()
    
    return student