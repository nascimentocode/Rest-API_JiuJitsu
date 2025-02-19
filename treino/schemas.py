from ninja import ModelSchema, Schema
from .models import Students
from typing import Optional

class StudentsSchema(ModelSchema):
    class Meta:
        model = Students
        fields = ["name", "email", "belt", "birthdate"]

class ProgressStudentSchema(Schema):
    email: str
    nome: str
    belt: str
    total_class: int
    classes_required_for_next_belt: int

class ClassHeldSchema(Schema):
    qtd: Optional[int]
    student_email: str