class BMI:
    def __init__(self, weight_pounds, height_feet):
        self.weight = weight_pounds
        self.height = height_feet

    def bmi_value(self):
        height_meter = self.height * 0.3048
        weight_kg = self.weight * 0.453592
        return weight_kg / (height_meter ** 2)

    def __eq__(self, other):
        if isinstance(other, BMI):
            return self.weight == other.weight and self.height == other.height
        return False

bmi1 = BMI(160, 5.8)
bmi2 = BMI(200, 6.5)

print("BMI 1:", bmi1.bmi_value())
print("BMI 2:", bmi2.bmi_value())
print("BMI 1 equals BMI 2:", bmi1 == bmi2)
