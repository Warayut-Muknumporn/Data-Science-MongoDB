# Data-Science-MongoDB

This project is part of foundation of data science about Data Processing

This coursework will assess your understanding of using NoSQL to store and retrieve data. You will perform operations on data from a collection of scientific articles in a MongoDB database. You will be required to run code to answer the given questions in the Jupyter notebook provided.

Download the dataset articles.json from Blackboard and import it into a collection called 'articles' into the 'coursework' database. The Virtual Machine comes pre-configured with an user "coursework" with password "coursework" with read-write privileges over the coursework database. The admin database is also 'coursework'.

Each question asks you to implement a function following a certain specification. We have an evaluation script that will check the correctness of your answer. It is essential that:

You respect the requested answer format, otherwise, the script will flag your answer as incorrect. If the result is correct, but your formatting is incorrect, you get a penalty of -20% of the mark.

Do not insert or delete cells in the notebook you will submit, the evaluation script relies on your answer being in the right cell.

If you feel the need of inserting cells to prepare and test your answer, do it in a copy of the notebook. Once you finish an answer that fits in a single cell, transfer it to the notebook that you will submit.

You can define auxiliary functions if you want, as long as they are all in the same cell as the main function.

If you add print statements for testing, please delete or comment them before submitting.

Answers can make use of the tools you learned so far: MongoDB pipelines and operators, Python code, pandas and networkx. An important aspect of the coursework is to identify in what situations is best to use MongoDB only, and in what situations is best to use multiple tools. A bad choice may make your answer less efficient, and in some cases, not run at all. The marking scheme at the end of the notebook details the expected execution times of your answers. Less efficient answers will get less marks.
