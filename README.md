# Manatal Schools and Students API

#### Ma. Micah Encarnacion
#### Senior Backend Developer
<br>

### Hours Spent
#### **Setup**: 4 hours
#### **Step 1**: 8 hours
#### **Step 2**: 4 hours
#### **Step 3**: 4 hours
#### **Additional Features/Bonus**: 4 hours
<br>

### Features
| URL | Method | Description |
| ----------- | ----------- | ----------- |
| `/schools` | `GET, POST` | Retrieve and create new schools with maximum number of students |
| `/schools/:id` | `GET, PUT, PATCH, DELETE` | Retrieve, update, or delete school item |
| `/schools/:id/students` | `GET, POST` | Retrieve students and create new student under a school instance |
| `/schools/:id/students/:student_id` | `GET, PUT, PATCH, DELETE` | Retrieve, update, or delete student item |
<br>

### Additional Checks/Features
* Added `nationality` and  `birthdate` as `Student` attribute
* `age` is not saved to database but calculated and returned every call to `/schools/:id/students` and `/schools/:id/students/:student_id`
* Error is returned when the maximum number of students is reached for a school instance.
* If the school ID passed to the URL is not equal to the school ID in the body, the student cannot be created.
* A student counter is added to the school instance on every create of a student to segregate students from different schools. The student ID is formatted as `{year student has been admitted}{school ID}{incremented student counter}`.
* The maximum number of students is validated if it is equal to or lower than 0. If it is, a DRF error is returned.