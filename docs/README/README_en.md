# 🔥 Modakbul (Campfire)

**2026-Spring Software Engineering Team Project**

**Instructor:** Jaekwon Lee

---

## 👨‍💻 Team Members & Roles

| Name | Role & Responsibilities | GitHub Profile |
| --- | --- | --- |
| **Geonwoo Kim** | Role 1 / ~ | [Github Profile](https://github.com/goukimesatz) |
| **Yerdos Narzhigitov** | Role 2 / ~ | [Github Profile](https://github.com/YerdosNar) |
| **Sangjun Jeon** | Role 3 / ~ | [Github Profile](https://github.com/nclsang) |
| **Kyungho Cha** | Role 4 / ~ | [Github Profile](https://github.com/Homeria) |

---

## 📖 Project Overview

**Modakbul (Campfire)** is an anonymous community backend API that enables dense, real-time communication on currently trending issues.

Every Topic (Campfire) is granted a default lifespan of 1 hour upon creation. If users continuously add 'Comments (Firewood)', the lifespan is incrementally extended by a variable burn rate algorithm. However, once public interest cools and the post reaches the end of its lifespan, it is permanently and automatically deleted from the database. Through this, only the freshest and most actively discussed topics remain whenever you log in.

---

## 🎯 Project Vision Statement

- **Target Users:** Anonymous users who feel burdened by permanent digital footprints and want to communicate lightly about real-time issues.
- **Problem or Need:** Existing communities permanently preserve written posts, leading to information fatigue and leaving unnecessary traces.
- **Product Category:** Real-time volatile anonymous community API server.
- **Key Benefit & Differentiation:** Assigns a 'lifespan' (`expires_at`) to posts, and completely eradicates posts with no participation from the database without a trace through Lazy Deletion and background physical deletion.

---

## 📌 Project Goals & Scope

- **Business Goals:** Optimization of system resources and processing of volatile data through the variable burn rate algorithm and transaction control.
- **In-Scope (Major Features):**
    - JWT token-based user authentication and authorization (Signup/Login)
    - RESTful API implementation for creating Topics (Campfire) and adding Comments (Firewood)
    - Active feed retrieval based on Lazy Deletion (`WHERE expires_at > now()`) utilizing DB queries (Raw SQL)
    - Application of a 'variable burn rate' algorithm where the lifespan extension time gradually decreases depending on the accumulated number of comments
    - Background scheduler (APScheduler) to periodically and physically remove expired data completely
- **Out-of-Scope:**
    - Complex frontend UI/UX implementation
    - Archiving system for permanent preservation of deleted posts
    - WebSocket-based real-time data push (replaced by a REST API optimized for read performance)

---

## 👥 Stakeholders & Users

- **Stakeholders:** Development team (all members), Professor, and TAs.
- **Requirements:** Structural validity verification on how the backend architecture controls concurrency issues (Race Conditions) and how efficiently it queries and cleans up volatile data.
- **Users:** Users who want to enjoy hot issue discussions without leaving a trace.

---

## 📅 Milestones

- **Milestone 1: Core Architecture & Common Interface Setup (Week 1 ~ Week 2)**
    - **Goal:** DB schema design and finalization of the development contract (Pydantic Schemas) between API and DB teams
    - **Tasks:**
        - Design SQLite3-based relational DB schemas (`users`, `topics`, `comments`) and create an ERD
        - Establish independent development environments between teams by defining data I/O forms (Pydantic `BaseModel`)
        - Initial FastAPI server environment setup and Router/CRUD skeleton code setup
        - Configuration of JWT secret key and one-way encryption (bcrypt) environment
    - **Deliverables:** DB schema generation script (`init_db.py`), API/CRUD interface definition document
        
- **Milestone 2: Parallel Development of Domain APIs & DB Raw Queries (Week 3 ~ Week 5)**
    - **Goal:** Implementation of actual business logic and endpoints for Auth, Topics, and Comments domains
    - **Tasks:**
        - **Auth:** Implementation of Signup/Login and JWT token issuance/verification middleware
        - **Topics:** Topic creation logic and active feed retrieval raw queries applying Lazy Deletion filtering (`WHERE expires_at > now()`)
        - **Comments:** Implementation of Comment addition applying a single transaction and the 'variable burn rate' lifespan extension algorithm
        - Centralization of exception handling via FastAPI global error handler (Custom Exceptions)
    - **Deliverables:** Integration-tested domain REST APIs (via Swagger UI)

- **Milestone 3: System Integration & Final Stabilization (Week 6 ~ Week 7)**
    - **Goal:** Garbage collector scheduler integration and overall system stabilization
    - **Tasks:**
        - Implementation of physical hard deletes (`DELETE`) for expired data utilizing asynchronous background tasks (APScheduler)
        - DB column index optimization to improve read performance
        - Conduct full API endpoint integration testing and check for concurrency issues
    - **Deliverables:** Final backend API server with integrated background tasks and team project final report
    
---

## 🛠 Tech Stack

- **Backend Framework:** FastAPI (Python 3.10.20)
- **Database & Data Access:** SQLite3 (Raw SQL queries using Python's built-in `sqlite3` module / No ORM)
- **Authentication & Security:** PyJWT, passlib[bcrypt]
- **Background Scheduler:** APScheduler
- **Deployment & Infra:** TBD (To Be Determined)
- **Development Tools:** Git / GitHub, VSCode, Pydantic (Data Validation)