'''
First Python code guided by mentor Abdul.
Created by Mayank (github.com/coder-daga)
　
It is a simple mental game using basic maths.
'''
　
import time
　
#Below function calculates the users intitally selected number
　
def initialnum(userans):
	initno=int(userans/100)-1;
	return (initno);
　
#Below function validates users calculations
　
def validate(userans): 
	if userans%100==60 :
		return True
	else:
		return False
	
def game():
	print("\n\nThink of a number between 1 and 10.\n\n");
　
	itr=[2,5,10];
	for num in itr:
		print("Now, multiply by "+str(num)+ " and then add "+str(num)+" to the result\n\n"); #print instructions to user
		time.sleep(3);
	ready=input("Enter 'done' if you're ready with your answer: ").lower(); #confirm with user if calculations are done. Human brain is not as fast as CPU.
	if ready=="done":
		userans=int(input("Enter your final answer:\t")); #Accept users calculated answer
		
	if(validate(userans)): #If validation is successful, invoke the function with calculates initial number taken by user
		print("Your number is:\t"+str(initialnum(userans)));
	else:
		print("\nLearn basics of mathematics!\n"); #If validation fails, prompt error
	return;
　
print ("************Welcome to the Game of Prediction************\n");
　
choice=1;
while(choice==1): #If choice is 1, only then execute game.
	game();
	choice=int(input("Do you want to play the game? Enter 1 for YES and 0 for NO:\t"));
exit();
　
