SELECT MAX(MONTHS * SALARY), COUNT(NAME) FROM EMPLOYEE
WHERE (MONTHS * SALARY) = (SELECT MAX(MONTHS * SALARY) FROM EMPLOYEE)