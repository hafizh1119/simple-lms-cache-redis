# STEP LANGKAH LANGKAH

### 1. docker-compose build
<img width="1117" height="533" alt="Cuplikan layar 2026-04-25 153610" src="https://github.com/user-attachments/assets/8a0db102-8e47-4cb1-8568-7b46c225b111" />

### 2. docker-compose up -d
<img width="1115" height="112" alt="Cuplikan layar 2026-04-25 153643" src="https://github.com/user-attachments/assets/924f92bf-cae3-4102-a3f2-039ae1a96f3b" />

### 3. docker-compose exec app python manage.py makemigrations
<img width="1151" height="225" alt="Cuplikan layar 2026-04-25 153915" src="https://github.com/user-attachments/assets/ed7e67bf-e845-4aea-8038-f5dc0eedeb51" />

### 4. docker-compose exec app python manage.py migrate
<img width="1133" height="116" alt="image" src="https://github.com/user-attachments/assets/058bdc64-e433-4053-a28b-a048bd2071c0" />


### 5. jalankan di browser : http://localhost:8000/api/docs#/
<img width="947" height="926" alt="Cuplikan layar 2026-04-25 151546" src="https://github.com/user-attachments/assets/5e157a6f-0d9d-4176-a3a9-c5ff2420d189" />

# Authentication:

### 1. POST /api/auth/register 
<img width="1309" height="815" alt="Cuplikan layar 2026-04-25 162724" src="https://github.com/user-attachments/assets/dea0ef75-701d-4960-aca7-2a2aadc2162a" />

### 2. POST /api/auth/login 
<img width="1382" height="709" alt="Cuplikan layar 2026-04-25 162807" src="https://github.com/user-attachments/assets/d2149796-9c1a-4470-aea4-d3ad2d0ca912" />
<img width="1918" height="1013" alt="Cuplikan layar 2026-04-25 210833" src="https://github.com/user-attachments/assets/b5ebd0f0-0b4e-4119-8ec2-35c9bd25bdb5" />

### 3. POST /api/auth/refresh 
<img width="1128" height="594" alt="Cuplikan layar 2026-04-25 165608" src="https://github.com/user-attachments/assets/46a935ca-6bc7-47ae-aa21-a43412376403" />

### 4. GET /api/auth/me
<img width="1468" height="785" alt="Cuplikan layar 2026-04-25 204300" src="https://github.com/user-attachments/assets/5428e62e-c132-400b-b3ca-de3505fe18ee" />

### 5. PUT /api/auth/me 
<img width="1389" height="737" alt="image" src="https://github.com/user-attachments/assets/a2899355-fe92-4b0e-88e9-6e768ef269a4" />

# Courses (Public):

### 1. GET /api/courses
<img width="1390" height="686" alt="image" src="https://github.com/user-attachments/assets/8430e0fc-905e-4e6b-a83e-e18f3e2fa524" />

### 2. GET /api/courses/{id} 
<img width="1388" height="728" alt="image" src="https://github.com/user-attachments/assets/f97de14c-48e7-459a-a5ee-3aa26b45a8f1" />

# Courses (Protected):

### 1. POST /api/courses  
<img width="1395" height="796" alt="Cuplikan layar 2026-04-25 230501" src="https://github.com/user-attachments/assets/c803102a-9287-4f0e-8459-5b5e98e84db1" />

### 2. PATCH /api/courses/{id}  
   <img width="1371" height="704" alt="Cuplikan layar 2026-04-25 231102" src="https://github.com/user-attachments/assets/cc8c3e77-951f-46bc-913e-1b2fc0b7fc8e" />

### 3. DELETE /api/courses/{id}  
   <img width="1450" height="837" alt="Cuplikan layar 2026-04-25 231430" src="https://github.com/user-attachments/assets/205b320a-9f60-4654-8974-7bbddf200fcb" />

# Enrollments:

### 1. POST /api/enrollments (Student)
<img width="1441" height="753" alt="Cuplikan layar 2026-04-25 232526" src="https://github.com/user-attachments/assets/5464ac7d-4cc4-4b75-8941-cbf3c710404a" />

### 2. GET /api/enrollments/my-courses 
<img width="1416" height="859" alt="Cuplikan layar 2026-04-25 232728" src="https://github.com/user-attachments/assets/3482607d-573e-435b-a35d-c721fd8d838e" />

### 3. POST /api/enrollments/{id}/progress 
<img width="1357" height="732" alt="Cuplikan layar 2026-04-25 233649" src="https://github.com/user-attachments/assets/4dc14aeb-9d13-491c-9c67-7709e026952f" />


### CEK POSTMAN
<img width="1449" height="862" alt="Cuplikan layar 2026-04-25 233940" src="https://github.com/user-attachments/assets/f157dc06-1918-4bad-8887-394fe1ca885b" />





