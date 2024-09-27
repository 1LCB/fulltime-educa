# coding: utf-8
from sqlalchemy import Column, Date, Enum, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Group(Base):
    __tablename__ = 'groups'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))


class Permission(Base):
    __tablename__ = 'permissions'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))


class School(Base):
    __tablename__ = 'schools'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))


class Sector(Base):
    __tablename__ = 'sectors'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))


class GroupPermission(Base):
    __tablename__ = 'group_permissions'

    id = Column(Integer, primary_key=True)
    group_id = Column(ForeignKey('groups.id', ondelete='CASCADE'), nullable=False, index=True)
    permission_id = Column(ForeignKey('permissions.id', ondelete='CASCADE'), nullable=False, index=True)

    group = relationship('Group')
    permission = relationship('Permission')


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    email = Column(String(100))
    password = Column(String(255))
    group_id = Column(ForeignKey('groups.id', ondelete='CASCADE'), index=True)
    image_path = Column(String(255))

    group = relationship('Group')


class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey('users.id', ondelete='CASCADE'), index=True)
    date_of_birth = Column(Date)
    gender = Column(Enum('male', 'female', 'other'))
    ethnicity = Column(String(50))
    birth_city = Column(String(100))
    id_card = Column(String(20))
    cpf = Column(String(11))
    phone = Column(String(20))
    address = Column(String(255))
    residential_complement = Column(String(255))
    father_name = Column(String(100))
    mother_name = Column(String(100))
    school_attended = Column(ForeignKey('schools.id'), index=True)
    current_school = Column(ForeignKey('schools.id'), index=True)
    shift = Column(String(50))
    sector_id = Column(ForeignKey('sectors.id'), index=True)
    admission_date = Column(Date)
    completion_date = Column(Date)
    course_status = Column(String(50))
    total_classes = Column(Integer)
    attendances = Column(Integer)
    absences = Column(Integer)

    school = relationship('School', primaryjoin='Student.current_school == School.id')
    school1 = relationship('School', primaryjoin='Student.school_attended == School.id')
    sector = relationship('Sector')
    user = relationship('User')


class Teacher(Base):
    __tablename__ = 'teachers'

    id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey('users.id', ondelete='SET NULL'), index=True)
    phone = Column(String(255))
    address = Column(String(255))

    user = relationship('User')


class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    teacher_id = Column(ForeignKey('teachers.id', ondelete='SET NULL'), index=True)

    teacher = relationship('Teacher')


class Class(Base):
    __tablename__ = 'classes'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    teacher_id = Column(ForeignKey('teachers.id', ondelete='SET NULL'), index=True)
    status = Column(Enum('active', 'inactive', 'other_option'))
    course_id = Column(ForeignKey('courses.id', ondelete='SET NULL'), index=True)

    course = relationship('Course')
    teacher = relationship('Teacher')


class Evaluation(Base):
    __tablename__ = 'evaluations'

    id = Column(Integer, primary_key=True)
    student_id = Column(ForeignKey('students.id', ondelete='CASCADE'), index=True)
    class_id = Column(ForeignKey('classes.id', ondelete='CASCADE'), index=True)
    sector_id = Column(ForeignKey('sectors.id', ondelete='CASCADE'), index=True)
    total_classes = Column(Integer)
    attendance = Column(Integer)
    absences = Column(Integer)

    _class = relationship('Class')
    sector = relationship('Sector')
    student = relationship('Student')


class StudentsClass(Base):
    __tablename__ = 'students_classes'

    id = Column(Integer, primary_key=True)
    student_id = Column(ForeignKey('students.id', ondelete='CASCADE'), index=True)
    class_id = Column(ForeignKey('classes.id', ondelete='CASCADE'), index=True)

    _class = relationship('Class')
    student = relationship('Student')
