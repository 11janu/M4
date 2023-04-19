<table><tr><td> <em>Assignment: </em> M4-Simple-Calc</td></tr>
<tr><td> <em>Student: </em> Jahnavi Soman (js2679)</td></tr>
<tr><td> <em>Generated: </em> 4/19/2023 2:54:19 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/m4-simple-calc/grade/js2679" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <p>Make sure you're working in an up to date branch</p><ul><li><code>git checkout dev</code></li><li><code>git pull origin dev</code></li><li><code>git checkout -b M4-Simple-Calc</code></li></ul><p>This will likely be started in class.</p><p>Steps:</p><ol><li>Create a new Folder called M4</li><li>Create a new file called MyCalc.py inside this folder</li><li>Create a MyCalc Class</li><li>Define basic addition / subtraction / multiplication / division functions<ol><li>These functions should update an internal variable as a running total/value called&nbsp;<code><b>ans</b></code></li><li>All functions must properly handle the math given standard math scenarios (i.e., show proper messages when trying to divide by zero for example)</li><li>Since you'll likely be taking screenshots of the code, make sure you add a comment with your ucid and the date</li></ol></li><li>Define a "main" logic to run when the program runs</li><li>This logic should ask for user input<ol><li>The input can be any valid number, any valid math operator, and any valid number (i.e., 2 * 2)<ol><li>This will do an immediate calculation, print it, and store the answer in the&nbsp;<code>ans</code>&nbsp;variable</li></ol></li><li>Alternatively, the input can be&nbsp;<code>ans</code>, any valid math operator, any valid number (i.e.,&nbsp;<code>ans</code>&nbsp;* 2)<ol><li>This will use the previous answer (or 0 if not set) as part of the calculation, print it, and will store the new answer in the&nbsp;<code>ans</code>&nbsp;variable</li></ol></li></ol></li><li>Create a test case for each scenario that utilize functions to have expected input and compare against expected output, all cases should pass (test cases should have a series of data passed into them)<ol><li>Test number-add-number</li><li>Test ans-add-number</li><li>Test number-sub-number</li><li>Test ans-sum-number</li><li>Test number-mult-number</li><li>Test ans-mult-number</li><li>Test number-div-number</li><li>Test ans-div-number</li></ol></li><li>Create a new file called m4_submission.md inside the M4 folder</li><li>Fill out the below deliverables</li><li>Generate the markdown and paste it into the m4_submission.md</li><li><code>git add .</code></li><li><code>git commit -m "adding m4 hw"</code></li><li><code>git push origin M4-Simple-Calc</code></li><li>Create a pull request M4-Simple-Calc to dev</li><li>Create a pull request dev to prod (after the previous one is merged)</li><li>Navigate to the prod branch on github, go to the M4 folder, click the m4_submission.md</li><li>Submit this link to Canvas</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Code Snippets (Make sure each screenshot has a comment showing your ucid and the date it was written) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of valid Addition Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113053/233025777-4bff2b2f-bec9-4f0a-9a47-855606764ab8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This is the function to add numbers. The output is shown below<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshot of valid Subtraction Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113053/233025902-c924209a-f85f-4936-a60b-01e194388b54.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This is the function to subtract numbers, output is shown below<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of valid Multiplication Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113053/233025907-97463b22-f727-4b87-9a80-9ba82ed2ea62.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This is the function to multiply numbers, output is shown below<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Screenshot of valid division Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113053/233025910-2a827ab0-20e3-44b1-87d7-a88fd2160b21.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This is the function to divide numbers, output is shown below<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Test Case Validations </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of passing number-add-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113053/233018381-9b6c2767-ac20-4227-8e59-3d1a3f1ddd78.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>3 test cases to show the addition of number and number.This testcase is<br>passed using pytest<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of passing ans-add-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113053/233018386-1da3922e-9d32-406c-ba75-1f236326d6a9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>3 passed testcases which shows the successful addition of previous answer and a<br>number <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of passing number-sub-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113053/233018390-5cea9386-2fa1-45b1-a8f2-a319e4ab8e6c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>3 passed test cases that shows the subtraction of 2 numbers<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Screenshots of passing ans-sub-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113053/233018394-90d2a637-4f7e-4ae3-975f-b1600daeb0b6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>3 passed test cases that shows the subtraction of previous answer and a<br>number<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Screenshots of passing number-mult-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113053/233018397-253bd36b-1aa9-4ee4-80eb-810a74280b6c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>3 passed test cases that shows the multiplication of two numbers<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 6: </em> Screenshots of passing ans-multi-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113053/233018399-1a0aaf83-25ea-4aaa-9bcc-f4f0427a10b3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>3 passed test cases that shows the multiplication of previous answer with a<br>number<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 7: </em> Screenshots of passing number-div-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113053/233018400-2a511208-6818-4136-9e6c-9f59ff014964.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>3 passes test cases that show the division between 2 numbers<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 8: </em> Screenshots of passing ans-div-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113053/233018403-91d9f701-05ef-46f9-8a86-fd5a5155b0e4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>3 passed test cases that shows the division of previous answer with a<br>number<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113053/233022625-ff241d62-53cc-4d33-8a8c-741c82d59249.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows all the passed test cases using pytest -rA<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Briefly talk about anything you learn during this assignment/module</td></tr>
<tr><td> <em>Response:</em> <p>I have learnt to execute a python code which calculates simple mathematical functions<br>such as addition, multiplication, subtractions, divisions.<div>I have also learnt using pytest and assert<br>statements.I have also gone through adding , pushing things into the github</div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Discuss how test cases work and anything new you learned about them while doing this assignment</td></tr>
<tr><td> <em>Response:</em> <p>Test cases are used to verify the correctness of a program. They are<br>designed to test the various features and functionalities of the code and ensure<br>that it behaves as expected.<div>&nbsp;In this assignment, we learned how to write test<br>cases in Python using the pytest framework. We created a sample program that<br>implemented a simple calculator and wrote test cases for each of its functions.</div><div>One<br>new thing I learned about test cases during this assignment is that they<br>can be used to catch errors that would otherwise go unnoticed. By writing<br>test cases that cover various edge cases and scenarios, we can ensure that<br>the program is robust and handles unexpected inputs correctly.<br></div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the pull request of M4-Simple-Calc to Dev link</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/11janu/M4/pull/1">https://github.com/11janu/M4/pull/1</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/m4-simple-calc/grade/js2679" target="_blank">Grading</a></td></tr></table>