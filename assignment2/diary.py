# Task 1: Diary
import traceback
import os

try:
    with open(os.path.curdir + os.sep + os.path.basename("diary.txt"), "a") as diary:
        prompt = "What happened today? "
        while True:
            line = input(prompt)
            diary.write(line + "\n")            
            diary.flush()            
            if line.lower().strip() == "done for now":
                break

            prompt = "What else? "

except Exception as e:
    trace_back = traceback.extract_tb(e.__traceback__)
    stack_trace = list()
    for trace in trace_back:
        stack_trace.append(
            f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}'
        )

    print(f"Exception type: {type(e).__name__}")
    message = str(e)
    if message:
        print(f"Exception message: {message}")
    print(f"Stack trace: {stack_trace}") 
    
