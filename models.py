from sqlalchemy import Column, Integer, String, Float, ForeignKey, Date
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()


class Customer(Base):
    __tablename__ = 'customers'

    customerID = Column(Integer, primary_key=True)
    firstName = Column(String)
    lastName = Column(String)
    email = Column(String)

    rentals = relationship("Rental", back_populates="customer")


class Car(Base):
    __tablename__ = 'cars'

    carID = Column(Integer, primary_key=True)
    brand = Column(String)
    model = Column(String)
    year = Column(Integer)
    pricePerDay = Column(Float)

    rentals = relationship("Rental", back_populates="car")


class Rental(Base):
    __tablename__ = 'rentals'

    rentalID = Column(Integer, primary_key=True)

    customerID = Column(Integer, ForeignKey('customers.customerID'))
    carID = Column(Integer, ForeignKey('cars.carID'))

    startDate = Column(Date)
    endDate = Column(Date)

    totalPrice = Column(Float)

    customer = relationship("Customer", back_populates="rentals")
    car = relationship("Car", back_populates="rentals")