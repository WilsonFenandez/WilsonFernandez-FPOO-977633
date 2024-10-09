# Clase Hospital
class Hospital:
    def __init__(self, nombre):
        self.nombre = nombre
        self.doctores = []
        self.pacientes = []

    def agregar_doctor(self, doctor):
        self.doctores.append(doctor)

    def agregar_paciente(self, paciente):
        self.pacientes.append(paciente)

    def listar_doctores(self):
        return [f"{doctor.nombre} - Especialidad: {Doctor.especialidades[doctor.especialidad]}" for doctor in self.doctores]

    def listar_pacientes(self):
        return [f"{paciente.nombre}, Edad: {paciente.edad}" for paciente in self.pacientes]

# Clase Paciente
class Paciente:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.historial_clinico = []

    def agregar_historial(self, cita):
        self.historial_clinico.append(cita)

    def listar_historial(self):
        return [cita.get_info() for cita in self.historial_clinico]

# Clase CitaMedica
class CitaMedica:
    def __init__(self, fecha, doctor, paciente):
        self.fecha = fecha
        self.doctor = doctor
        self.paciente = paciente

    def get_info(self):
        return f"Cita médica - Fecha: {self.fecha}, Doctor: {self.doctor.nombre}, Paciente: {self.paciente.nombre}"

# Clase Doctor
class Doctor:
    especialidades = {1: "Cardiología", 2: "Neurología", 3: "Pediatría", 4: "Ginecología"}

    def __init__(self, nombre, especialidad):
        self.nombre = nombre
        self.especialidad = especialidad
        self.citas = []

    def asignar_cita(self, paciente, fecha):
        cita = CitaMedica(fecha, self, paciente)
        self.citas.append(cita)
        paciente.agregar_historial(cita)
        return f"Cita asignada: {cita.get_info()}"

    def listar_citas(self):
        return [cita.get_info() for cita in self.citas]
