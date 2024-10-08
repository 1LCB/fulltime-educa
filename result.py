from typing import List, Optional

from sqlalchemy import Column, Date, Enum, ForeignKeyConstraint, Index, String
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.orm import Mapped, declarative_base, mapped_column, relationship
from sqlalchemy.orm.base import Mapped

Base = declarative_base()


class Groups(Base):
    __tablename__ = 'groups'

    ID = mapped_column(INTEGER(11), primary_key=True)
    NAME = mapped_column(String(100))

    group_permissions: Mapped[List['GroupPermissions']] = relationship('GroupPermissions', uselist=True, back_populates='groups')
    users: Mapped[List['Users']] = relationship('Users', uselist=True, back_populates='groups')


class Permissions(Base):
    __tablename__ = 'permissions'

    ID = mapped_column(INTEGER(11), primary_key=True)
    NAME = mapped_column(String(100))

    group_permissions: Mapped[List['GroupPermissions']] = relationship('GroupPermissions', uselist=True, back_populates='permissions')


class Schools(Base):
    __tablename__ = 'schools'

    ID = mapped_column(INTEGER(11), primary_key=True)
    NAME = mapped_column(String(100))

    students: Mapped[List['Students']] = relationship('Students', uselist=True, foreign_keys='[Students.CURRENT_SCHOOL]', back_populates='schools')
    students_: Mapped[List['Students']] = relationship('Students', uselist=True, foreign_keys='[Students.SCHOOL_ATTENDED]', back_populates='schools_')


class Sectors(Base):
    __tablename__ = 'sectors'

    ID = mapped_column(INTEGER(11), primary_key=True)
    NAME = mapped_column(String(100))

    students: Mapped[List['Students']] = relationship('Students', uselist=True, back_populates='sectors')
    evaluations: Mapped[List['Evaluations']] = relationship('Evaluations', uselist=True, back_populates='sectors')


class Teachers(Base):
    __tablename__ = 'teachers'

    ID = mapped_column(INTEGER(11), primary_key=True)
    CPF = mapped_column(String(11))

    courses: Mapped[List['Courses']] = relationship('Courses', uselist=True, back_populates='teachers')
    classes: Mapped[List['Classes']] = relationship('Classes', uselist=True, back_populates='teachers')


class Courses(Base):
    __tablename__ = 'courses'
    __table_args__ = (
        ForeignKeyConstraint(['TEACHER_ID'], ['teachers.ID'], ondelete='SET NULL', name='courses_ibfk_1'),
        Index('TEACHER_ID', 'TEACHER_ID')
    )

    ID = mapped_column(INTEGER(11), primary_key=True)
    NAME = mapped_column(String(100))
    TEACHER_ID = mapped_column(INTEGER(11))

    teachers: Mapped[Optional['Teachers']] = relationship('Teachers', back_populates='courses')
    classes: Mapped[List['Classes']] = relationship('Classes', uselist=True, back_populates='courses')


class GroupPermissions(Base):
    __tablename__ = 'group_permissions'
    __table_args__ = (
        ForeignKeyConstraint(['GROUP_ID'], ['groups.ID'], ondelete='CASCADE', name='group_permissions_ibfk_1'),
        ForeignKeyConstraint(['PERMISSION_ID'], ['permissions.ID'], ondelete='CASCADE', name='group_permissions_ibfk_2'),
        Index('GROUP_ID', 'GROUP_ID'),
        Index('PERMISSION_ID', 'PERMISSION_ID')
    )

    ID = mapped_column(INTEGER(11), primary_key=True)
    GROUP_ID = mapped_column(INTEGER(11), nullable=False)
    PERMISSION_ID = mapped_column(INTEGER(11), nullable=False)

    groups: Mapped['Groups'] = relationship('Groups', back_populates='group_permissions')
    permissions: Mapped['Permissions'] = relationship('Permissions', back_populates='group_permissions')


class Users(Base):
    __tablename__ = 'users'
    __table_args__ = (
        ForeignKeyConstraint(['GROUP_ID'], ['groups.ID'], ondelete='CASCADE', name='users_ibfk_1'),
        Index('GROUP_ID', 'GROUP_ID')
    )

    ID = mapped_column(INTEGER(11), primary_key=True)
    NAME = mapped_column(String(100))
    EMAIL = mapped_column(String(100))
    PASSWORD = mapped_column(String(255))
    GROUP_ID = mapped_column(INTEGER(11))
    IMAGE_PATH = mapped_column(String(255))

    groups: Mapped[Optional['Groups']] = relationship('Groups', back_populates='users')
    students: Mapped[List['Students']] = relationship('Students', uselist=True, back_populates='users')


class Classes(Base):
    __tablename__ = 'classes'
    __table_args__ = (
        ForeignKeyConstraint(['COURSE_ID'], ['courses.ID'], ondelete='SET NULL', name='classes_ibfk_2'),
        ForeignKeyConstraint(['TEACHER_ID'], ['teachers.ID'], ondelete='SET NULL', name='classes_ibfk_1'),
        Index('COURSE_ID', 'COURSE_ID'),
        Index('TEACHER_ID', 'TEACHER_ID')
    )

    ID = mapped_column(INTEGER(11), primary_key=True)
    NAME = mapped_column(String(100))
    TEACHER_ID = mapped_column(INTEGER(11))
    STATUS = mapped_column(Enum('active', 'inactive', 'other_option'))
    COURSE_ID = mapped_column(INTEGER(11))

    courses: Mapped[Optional['Courses']] = relationship('Courses', back_populates='classes')
    teachers: Mapped[Optional['Teachers']] = relationship('Teachers', back_populates='classes')
    evaluations: Mapped[List['Evaluations']] = relationship('Evaluations', uselist=True, back_populates='classes')
    students_classes: Mapped[List['StudentsClasses']] = relationship('StudentsClasses', uselist=True, back_populates='classes')


class Students(Base):
    __tablename__ = 'students'
    __table_args__ = (
        ForeignKeyConstraint(['CURRENT_SCHOOL'], ['schools.ID'], name='students_ibfk_4'),
        ForeignKeyConstraint(['SCHOOL_ATTENDED'], ['schools.ID'], name='students_ibfk_3'),
        ForeignKeyConstraint(['SECTOR_ID'], ['sectors.ID'], name='students_ibfk_2'),
        ForeignKeyConstraint(['USER_ID'], ['users.ID'], ondelete='CASCADE', name='students_ibfk_1'),
        Index('CURRENT_SCHOOL', 'CURRENT_SCHOOL'),
        Index('SCHOOL_ATTENDED', 'SCHOOL_ATTENDED'),
        Index('SECTOR_ID', 'SECTOR_ID'),
        Index('USER_ID', 'USER_ID')
    )

    ID = mapped_column(INTEGER(11), primary_key=True)
    USER_ID = mapped_column(INTEGER(11))
    CLASS = mapped_column(String(100))
    DATE_OF_BIRTH = mapped_column(Date)
    GENDER = mapped_column(Enum('male', 'female', 'other'))
    ETHNICITY = mapped_column(String(50))
    BIRTH_CITY = mapped_column(String(100))
    ID_CARD = mapped_column(String(20))
    CPF = mapped_column(String(11))
    PHONE = mapped_column(String(20))
    ADDRESS = mapped_column(String(255))
    RESIDENTIAL_COMPLEMENT = mapped_column(String(255))
    FATHER_NAME = mapped_column(String(100))
    MOTHER_NAME = mapped_column(String(100))
    SCHOOL_ATTENDED = mapped_column(INTEGER(11))
    CURRENT_SCHOOL = mapped_column(INTEGER(11))
    CURRENT_COURSE = mapped_column(String(100))
    SHIFT = mapped_column(String(50))
    SECTOR_ID = mapped_column(INTEGER(11))
    ADMISSION_DATE = mapped_column(Date)
    COMPLETION_DATE = mapped_column(Date)
    COURSE_STATUS = mapped_column(String(50))
    TOTAL_CLASSES = mapped_column(INTEGER(11))
    ATTENDANCES = mapped_column(INTEGER(11))
    ABSENCES = mapped_column(INTEGER(11))

    schools: Mapped[Optional['Schools']] = relationship('Schools', foreign_keys=[CURRENT_SCHOOL], back_populates='students')
    schools_: Mapped[Optional['Schools']] = relationship('Schools', foreign_keys=[SCHOOL_ATTENDED], back_populates='students_')
    sectors: Mapped[Optional['Sectors']] = relationship('Sectors', back_populates='students')
    users: Mapped[Optional['Users']] = relationship('Users', back_populates='students')
    evaluations: Mapped[List['Evaluations']] = relationship('Evaluations', uselist=True, back_populates='students')
    students_classes: Mapped[List['StudentsClasses']] = relationship('StudentsClasses', uselist=True, back_populates='students')


class Evaluations(Base):
    __tablename__ = 'evaluations'
    __table_args__ = (
        ForeignKeyConstraint(['CLASS_ID'], ['classes.ID'], ondelete='CASCADE', name='evaluations_ibfk_2'),
        ForeignKeyConstraint(['SECTOR_ID'], ['sectors.ID'], ondelete='CASCADE', name='evaluations_ibfk_3'),
        ForeignKeyConstraint(['STUDENT_ID'], ['students.ID'], ondelete='CASCADE', name='evaluations_ibfk_1'),
        Index('CLASS_ID', 'CLASS_ID'),
        Index('SECTOR_ID', 'SECTOR_ID'),
        Index('STUDENT_ID', 'STUDENT_ID')
    )

    ID = mapped_column(INTEGER(11), primary_key=True)
    STUDENT_ID = mapped_column(INTEGER(11))
    CLASS_ID = mapped_column(INTEGER(11))
    SECTOR_ID = mapped_column(INTEGER(11))
    TOTAL_CLASSES = mapped_column(INTEGER(11))
    ATTENDANCE = mapped_column(INTEGER(11))
    ABSENCES = mapped_column(INTEGER(11))

    classes: Mapped[Optional['Classes']] = relationship('Classes', back_populates='evaluations')
    sectors: Mapped[Optional['Sectors']] = relationship('Sectors', back_populates='evaluations')
    students: Mapped[Optional['Students']] = relationship('Students', back_populates='evaluations')


class StudentsClasses(Base):
    __tablename__ = 'students_classes'
    __table_args__ = (
        ForeignKeyConstraint(['CLASS_ID'], ['classes.ID'], ondelete='CASCADE', name='students_classes_ibfk_2'),
        ForeignKeyConstraint(['STUDENT_ID'], ['students.ID'], ondelete='CASCADE', name='students_classes_ibfk_1'),
        Index('CLASS_ID', 'CLASS_ID'),
        Index('STUDENT_ID', 'STUDENT_ID')
    )

    ID = mapped_column(INTEGER(11), primary_key=True)
    STUDENT_ID = mapped_column(INTEGER(11))
    CLASS_ID = mapped_column(INTEGER(11))

    classes: Mapped[Optional['Classes']] = relationship('Classes', back_populates='students_classes')
    students: Mapped[Optional['Students']] = relationship('Students', back_populates='students_classes')
