CREATE DATABASE company_db;
USE company_db;
CREATE TABLE employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    position VARCHAR(255),
    department VARCHAR(255),
    hire_date DATE
);

CREATE TABLE tasks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    employee_id INT,
    task_description TEXT,
    status ENUM('Pending', 'In Progress', 'Completed'),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (employee_id) REFERENCES employees(id) ON DELETE CASCADE
);
INSERT INTO employees (name, position, department, hire_date) VALUES
('Ali Kamal', 'Software Engineer', 'IT', '2025-01-15'),
('Abeer Hany', 'Data Analyst', 'Data Science', '2021-09-10'),
('Khaled Mohamed', 'Project Manager', 'Operations', '2020-06-25'),
('Jana Ahmed', 'HR Specialist', 'Human Resources', '2019-04-30'),
('Mahmoud Saad', 'Marketing Executive', 'Marketing', '2023-02-20'),
('Hady karem', 'Marketing Executive', 'IT', '2023-02-20'),
('Omar Youssef', 'AI Researcher', 'Artificial Intelligence', '2025-03-29');

INSERT INTO tasks (employee_id, task_description, status) VALUES
(1, 'Develop API for mobile app', 'In Progress'),
(1, 'Fix backend authentication bug', 'Pending'),
(2, 'Analyze customer churn data', 'Completed'),
(2, 'Create dashboard for sales team', 'In Progress'),
(3, 'Prepare project a for Q3', 'Pending'),
(3, 'Conduct team meetings', 'Completed'),
(4, 'Interview new candidates', 'In Progress'),
(4, 'Update company policies', 'Pending'),
(5, 'Plan social media campaign', 'Completed'),
(5, 'Design new email marketing strategy', 'In Progress');
SELECT * FROM employees;
SELECT * FROM tasks;



