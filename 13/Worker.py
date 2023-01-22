class Worker:
    id: int
    age: int
    salary: int
    full_name: str
    dep_id: str

    def __init__(self, id: int, full_name: str, age: int, salary: int, dep_id: str) -> None:
        self.id = id
        self.full_name = full_name
        self.age = age
        self.salary = salary
        self.dep_id = dep_id

    def __repr__(self) -> str:
        return f'full_name: {self.full_name} id: {self.id} age: {self.age} salary: {self.salary} dep_id: {self.dep_id} '
