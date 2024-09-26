from sqlalchemy import String, Date, Enum, ForeignKeyConstraint, Index, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from infrastructure.database.mysql.settings.base import Base
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.orm import relationship
from sqlalchemy.orm.base import Mapped
from typing import List, Optional



class Groups(Base):
    __tablename__ = 'groups'

    id = mapped_column(INTEGER(11), primary_key=True)
    name = mapped_column(String(100))

    group_permissions: Mapped[List['GroupPermissions']] = relationship('GroupPermissions', uselist=True, back_populates='group')
    users: Mapped[List['Users']] = relationship('Users', uselist=True, back_populates='group')


class Permissions(Base):
    __tablename__ = 'permissions'

    id = mapped_column(INTEGER(11), primary_key=True)
    name = mapped_column(String(100))

    group_permissions: Mapped[List['GroupPermissions']] = relationship('GroupPermissions', uselist=True, back_populates='permission')


class Schools(Base):
    __tablename__ = 'schools'

    id = mapped_column(INTEGER(11), primary_key=True)
    name = mapped_column(String(100))

    students: Mapped[List['Students']] = relationship('Students', uselist=True, foreign_keys='[Students.current_school]', back_populates='schools')
    students_: Mapped[List['Students']] = relationship('Students', uselist=True, foreign_keys='[Students.school_attended]', back_populates='schools_')


class Sectors(Base):
    __tablename__ = 'sectors'

    id = mapped_column(INTEGER(11), primary_key=True)
    name = mapped_column(String(100))

    students: Mapped[List['Students']] = relationship('Students', uselist=True, back_populates='sector')
    evaluations: Mapped[List['Evaluations']] = relationship('Evaluations', uselist=True, back_populates='sector')


class GroupPermissions(Base):
    __tablename__ = 'group_permissions'
    __table_args__ = (
        ForeignKeyConstraint(['group_id'], ['groups.id'], ondelete='CASCADE', name='group_permissions_ibfk_1'),
        ForeignKeyConstraint(['permission_id'], ['permissions.id'], ondelete='CASCADE', name='group_permissions_ibfk_2'),
        Index('group_id', 'group_id'),
        Index('permission_id', 'permission_id')
    )

    id = mapped_column(INTEGER(11), primary_key=True)
    group_id = mapped_column(INTEGER(11), nullable=False)
    permission_id = mapped_column(INTEGER(11), nullable=False)

    group: Mapped['Groups'] = relationship('Groups', back_populates='group_permissions')
    permission: Mapped['Permissions'] = relationship('Permissions', back_populates='group_permissions')


class Users(Base):
    __tablename__ = 'users'
    __table_args__ = (
        ForeignKeyConstraint(['group_id'], ['groups.id'], ondelete='CASCADE', name='users_ibfk_1'),
        Index('group_id', 'group_id')
    )

    id = mapped_column(INTEGER(11), primary_key=True)
    name = mapped_column(String(100))
    email = mapped_column(String(100))
    password = mapped_column(String(255))
    group_id = mapped_column(INTEGER(11))
    image_path = mapped_column(String(255))

    group: Mapped[Optional['Groups']] = relationship('Groups', back_populates='users')
    students: Mapped[List['Students']] = relationship('Students', uselist=True, back_populates='user')
    teachers: Mapped[List['Teachers']] = relationship('Teachers', uselist=True, back_populates='user')


class Students(Base):
    __tablename__ = 'students'
    __table_args__ = (
        ForeignKeyConstraint(['current_school'], ['schools.id'], name='students_ibfk_4'),
        ForeignKeyConstraint(['school_attended'], ['schools.id'], name='students_ibfk_3'),
        ForeignKeyConstraint(['sector_id'], ['sectors.id'], name='students_ibfk_2'),
        ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE', name='students_ibfk_1'),
        Index('current_school', 'current_school'),
        Index('school_attended', 'school_attended'),
        Index('sector_id', 'sector_id'),
        Index('user_id', 'user_id')
    )

    id = mapped_column(INTEGER(11), primary_key=True)
    user_id = mapped_column(INTEGER(11))
    date_of_birth = mapped_column(Date)
    gender = mapped_column(Enum('male', 'female', 'other'))
    ethnicity = mapped_column(String(50))
    birth_city = mapped_column(String(100))
    id_card = mapped_column(String(20))
    cpf = mapped_column(String(11))
    phone = mapped_column(String(20))
    address = mapped_column(String(255))
    residential_complement = mapped_column(String(255))
    father_name = mapped_column(String(100))
    mother_name = mapped_column(String(100))
    school_attended = mapped_column(INTEGER(11))
    current_school = mapped_column(INTEGER(11))
    shift = mapped_column(String(50))
    sector_id = mapped_column(INTEGER(11))
    admission_date = mapped_column(Date)
    completion_date = mapped_column(Date)
    course_status = mapped_column(String(50))
    total_classes = mapped_column(INTEGER(11))
    attendances = mapped_column(INTEGER(11))
    absences = mapped_column(INTEGER(11))

    schools: Mapped[Optional['Schools']] = relationship('Schools', foreign_keys=[current_school], back_populates='students')
    schools_: Mapped[Optional['Schools']] = relationship('Schools', foreign_keys=[school_attended], back_populates='students_')
    sector: Mapped[Optional['Sectors']] = relationship('Sectors', back_populates='students')
    user: Mapped[Optional['Users']] = relationship('Users', back_populates='students')
    evaluations: Mapped[List['Evaluations']] = relationship('Evaluations', uselist=True, back_populates='student')
    students_classes: Mapped[List['StudentsClasses']] = relationship('StudentsClasses', uselist=True, back_populates='student')


class Teachers(Base):
    __tablename__ = 'teachers'
    __table_args__ = (
        ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='SET NULL', name='teachers_ibfk_1'),
        Index('user_id', 'user_id')
    )

    id = mapped_column(INTEGER(11), primary_key=True)
    cpf = mapped_column(String(11))
    user_id = mapped_column(INTEGER(11))

    user: Mapped[Optional['Users']] = relationship('Users', back_populates='teachers')
    courses: Mapped[List['Courses']] = relationship('Courses', uselist=True, back_populates='teacher')
    classes: Mapped[List['Classes']] = relationship('Classes', uselist=True, back_populates='teacher')


class Courses(Base):
    __tablename__ = 'courses'
    __table_args__ = (
        ForeignKeyConstraint(['teacher_id'], ['teachers.id'], ondelete='SET NULL', name='courses_ibfk_1'),
        Index('teacher_id', 'teacher_id')
    )

    id = mapped_column(INTEGER(11), primary_key=True)
    name = mapped_column(String(100))
    teacher_id = mapped_column(INTEGER(11))

    teacher: Mapped[Optional['Teachers']] = relationship('Teachers', back_populates='courses')
    classes: Mapped[List['Classes']] = relationship('Classes', uselist=True, back_populates='course')


class Classes(Base):
    __tablename__ = 'classes'
    __table_args__ = (
        ForeignKeyConstraint(['course_id'], ['courses.id'], ondelete='SET NULL', name='classes_ibfk_2'),
        ForeignKeyConstraint(['teacher_id'], ['teachers.id'], ondelete='SET NULL', name='classes_ibfk_1'),
        Index('course_id', 'course_id'),
        Index('teacher_id', 'teacher_id')
    )

    id = mapped_column(INTEGER(11), primary_key=True)
    name = mapped_column(String(100))
    teacher_id = mapped_column(INTEGER(11))
    status = mapped_column(Enum('active', 'inactive', 'other_option'))
    course_id = mapped_column(INTEGER(11))

    course: Mapped[Optional['Courses']] = relationship('Courses', back_populates='classes')
    teacher: Mapped[Optional['Teachers']] = relationship('Teachers', back_populates='classes')
    evaluations: Mapped[List['Evaluations']] = relationship('Evaluations', uselist=True, back_populates='class_')
    students_classes: Mapped[List['StudentsClasses']] = relationship('StudentsClasses', uselist=True, back_populates='class_')


class Evaluations(Base):
    __tablename__ = 'evaluations'
    __table_args__ = (
        ForeignKeyConstraint(['class_id'], ['classes.id'], ondelete='CASCADE', name='evaluations_ibfk_2'),
        ForeignKeyConstraint(['sector_id'], ['sectors.id'], ondelete='CASCADE', name='evaluations_ibfk_3'),
        ForeignKeyConstraint(['student_id'], ['students.id'], ondelete='CASCADE', name='evaluations_ibfk_1'),
        Index('class_id', 'class_id'),
        Index('sector_id', 'sector_id'),
        Index('student_id', 'student_id')
    )

    id = mapped_column(INTEGER(11), primary_key=True)
    student_id = mapped_column(INTEGER(11))
    class_id = mapped_column(INTEGER(11))
    sector_id = mapped_column(INTEGER(11))
    total_classes = mapped_column(INTEGER(11))
    attendance = mapped_column(INTEGER(11))
    absences = mapped_column(INTEGER(11))

    class_: Mapped[Optional['Classes']] = relationship('Classes', back_populates='evaluations')
    sector: Mapped[Optional['Sectors']] = relationship('Sectors', back_populates='evaluations')
    student: Mapped[Optional['Students']] = relationship('Students', back_populates='evaluations')


class StudentsClasses(Base):
    __tablename__ = 'students_classes'
    __table_args__ = (
        ForeignKeyConstraint(['class_id'], ['classes.id'], ondelete='CASCADE', name='students_classes_ibfk_2'),
        ForeignKeyConstraint(['student_id'], ['students.id'], ondelete='CASCADE', name='students_classes_ibfk_1'),
        Index('class_id', 'class_id'),
        Index('student_id', 'student_id')
    )

    id = mapped_column(INTEGER(11), primary_key=True)
    student_id = mapped_column(INTEGER(11))
    class_id = mapped_column(INTEGER(11))

    class_: Mapped[Optional['Classes']] = relationship('Classes', back_populates='students_classes')
    student: Mapped[Optional['Students']] = relationship('Students', back_populates='students_classes')
