from random import randint

def generate_testbench(module_name, inputs, output, total_input_combination, input_width):
    # Testbench header with module name
    testbench = f"module {module_name}_tb;\n\n"
    
    # Declaring registers for inout ports
    for signal in inputs :
        if input_width>1:#if input were more than a bit long
            testbench += f"  [{input_width-1}: 0]reg {signal};\n"
        else:
            testbench += f"  reg {signal};\n"
            
    #Declaring wire for output port 
    for signal in output :
        if input_width>1:#if the output were more than a bit long
            testbench += f"  [{input_width-1}: 0]wire {signal};\n"
        else:
            testbench += f"  wire {signal};\n"
        
    
    # Instantiating the module
    testbench += f"\n  {module_name} uut ({', '.join(inputs)}, {', '.join(output)});\n\n"
    
    # stimulus block
    testbench += "  initial begin\n"
    
    #preparing input vectors for the test bench as tuple
    input_values = list(product([0, 1], repeat=input_width))
    input_array =[]
    
    #converting tuple to string for easy manipulation in later stages
    for str1 in input_values:
        string_representation = ''.join(map(str, str1))
        input_array.append(string_representation)
        
    count = 0    
    
    #feeding input sequence to the registers
    for i in input_array:
        
        
        for j in input_array:
            testbench += f"\n    // input test sequence-{count + 1}\n"
            count = count+1;
            testbench += f"\n    input_a = "+i+";";
            testbench += f"\n    input_b = "+j+";"
            #Adding delay between one inout sequence and another
            testbench += f"\n    #5; // 5 time units\n"
   
        
    # Monitoring the output through debug console
    testbench += f"\n    // Display output\n"
    testbench += f"    $display(\"Output: %b\", {output});\n"
    testbench += "  end\n\n"
    
    # End of testbench
    testbench += "endmodule\n"
    
    return testbench

# main instantiation of function generate_testbench()
#we are doing for simple and gate here
module_name = "and_gate"
inputs = ["input_a", "input_b"]
output = ["output_result"]
total_input_combination = 4*pow(2,input_width)
input_width=3

testbench_code = generate_testbench(module_name, inputs, output, total_input_combination,input_width)

print(testbench_code)
