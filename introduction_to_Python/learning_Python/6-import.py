import basic_functions


PEOPLE_PER_SQUARE_METER = 2
FIELD_LENGTH = 60
FIELD_WIDTH = 45
people_at_concert = (
    basic_functions.rectangle(FIELD_LENGTH, FIELD_WIDTH) * PEOPLE_PER_SQUARE_METER
)
print("Estão presentes no show aproximadamente", people_at_concert, "pessoas.")