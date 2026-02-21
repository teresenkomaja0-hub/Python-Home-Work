import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Student
from db import get_db
import contextlib

# Настраиваем тестовую базу данных (можно использовать ту же базу с отдельной таблицей)
TEST_DATABASE_URL = "postgresql://myuser:mypassword@localhost:5432/mydatabase"
test_engine = create_engine(TEST_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=test_engine)

# Создаем таблицы для теста
Base.metadata.create_all(bind=test_engine)

@pytest.fixture
def db_session():
    # Создаем новую сессию для теста
    connection = test_engine.connect()
    transaction = connection.begin()
    session = sessionmaker(bind=connection)()

    yield session

    # Чистим после теста
    session.close()
    transaction.rollback()
    connection.close()

# Тест на добавление
def test_create_student(db_session):
    student = Student(name="Тестовый студент", age=20)
    db_session.add(student)
    db_session.commit()

    assert student.id is not None

# Тест на изменение
def test_update_student(db_session):
    student = Student(name="Студент для изменения", age=22)
    db_session.add(student)
    db_session.commit()

    # Изменяем
    student.name = "Обновленный студент"
    db_session.commit()

    updated_student = db_session.query(Student).filter_by(id=student.id).first()
    assert updated_student.name == "Обновленный студент"

# Тест на удаление
def test_delete_student(db_session):
    student = Student(name="Студент для удаления", age=23)
    db_session.add(student)
    db_session.commit()

    # Удаляем
    db_session.delete(student)
    db_session.commit()

    deleted = db_session.query(Student).filter_by(id=student.id).first()
    assert deleted is None