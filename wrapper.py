import subprocess 
#C portion is completely taken from the Lab5 slides
#input array
input_array = ["1", "2", "3", "4", "5"]
# #compile C program that is named as cprog.c
# subprocess.run(["gcc", "cprog.c", "-o", "cprog"])
# #run compiled program with the input array as our argument
# process = subprocess.run(["./cprog"] + input_array, capture_output=1, text = True)
# #store the output of the c program into a variable
# output_variable = process.stdout.strip()

# #print or use stored output
print("C Program Output")
# print(output_variable)

# #Haskell outputs
subprocess.run(["ghc", "hprog.hs"])
process = subprocess.run(["./hprog"]+[str(x) for x in input_array], text = True, capture_output=True)
result = process.stdout.strip()

print("Haskell Program Output")
print(result)

# #prolog implementation
# prolog_input = "[" + ", ".join(map(str, input_array)) + "]."
# result = subprocess.run(['swipl', '-q', '-g', 'main', '-t', 'halt','pprog.pl'], input = prolog_input, capture_output = True, text = True)
# output_result = result.stdout.strip()
# print("Prolog Program output")
# print(output_result)

#MATLAB portion
print("Running MATLAB CODE 1")

matlab_executable = '/Program Files/MATLAB/R2023b/bin/matlab'
matlab_process = subprocess.run([matlab_executable, "-batch", "run('mprog1.m'); pause(1);"], capture_output=True)

#read values from input text file
with open('input.txt', 'r') as file:
    line = file.readline()
    input_array = [int(value) for value in line.split(",")]
    input_array = [str(value) for value in input_array]

#run C program with input_array we just made from input.txt
subprocess.run(["gcc", "cprog.c", "-o", "cprog"])
# #run compiled program with the input array as our argument
process = subprocess.run(["./cprog"] + input_array, capture_output=1, text = True)
# #store the output of the c program into a variable
output_variable = process.stdout.strip()
# #write to an output file
print(output_variable)
with open('c_output.txt', 'w') as f:
    f.write(output_variable)


# #run MATLAB program 2

print("Running MATLAB CODE 2")
matlab_process = subprocess.run([matlab_executable, "-batch", "run('mprog2.m'); pause(1);"], capture_output=True)