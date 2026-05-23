SELECT * FROM [Users];
SELECT * FROM [Users] WHERE [country] = 'Italy';
SELECT * FROM [Users] WHERE [city] = 'Florø';
SELECT * FROM [Users] WHERE [salary] > 5000;
SELECT * FROM [Users] WHERE [salary] < 2000;
SELECT * FROM [Users] WHERE [country] = 'Spain';
SELECT * FROM [Users] WHERE [email] LIKE '%outlook%';
SELECT * FROM [Users] WHERE [email] LIKE '%gmail%';
SELECT * FROM [Users] WHERE [surname] LIKE 'C%';
SELECT * FROM [Users] WHERE [name] LIKE '%a%';
SELECT * FROM [Users] WHERE [email] LIKE '%.com';
SELECT TOP 10 * FROM [Users] ORDER BY [salary] DESC;
SELECT TOP 10 * FROM [Users] ORDER BY [salary] ASC;
SELECT * FROM [Users] ORDER BY [country] ASC, [salary] DESC;
SELECT TOP 1 [name], [surname], [salary] FROM [Users] ORDER BY [salary] DESC;
SELECT TOP 1 [name], [surname], [salary] FROM [Users] ORDER BY [salary] ASC;
SELECT COUNT(*) AS [TotalUsers] FROM [Users];
SELECT AVG([salary]) AS [AverageSalary] FROM [Users];
SELECT MAX([salary]) AS [MaxSalary] FROM [Users];
SELECT MIN([salary]) AS [MinSalary] FROM [Users];
SELECT [country], COUNT(*) AS [UsersCount] 
FROM [Users] 
GROUP BY [country] 
ORDER BY [UsersCount] DESC;