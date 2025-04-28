# 26-04-25
'''
multi threading:
----------------
Multi threading is a way of achieving multi tasking. In multi threading, the concept
of threads is used...

What is process?
In computing, a process is an instance of a computer program that is being executed.
Any process has 3 basic components:
    1.An executable program
    2. The associated data needed by the program
    3. The execution context of the program (state of process)

An intro to threading:
-------------------
A thread is an entity within a process that can be scheduled for execution. Also, it
is the smallest unit of processing that can be performed in an Operating System.
A thread is a sequence of such instructions with in a program that can be executed
independently of the other code....
A thread contains all this information in "thread control block(tcb)"

Thread Identifier : Unique ID is assigned to every new thread

Stack Pointer : Points to the thread's stack in the process. The stack contains the
local variables under the thread's scope.

Program counter : A register that stores the address of the instruction currently
being executed by a thread.

Thread state : Can be running, ready, waiting, starting or done

Thread's register set : Registers assigned to thread for computations

Parent process pointer : A pointer to the process control block(pcb) of the process
that thread lives on...

Multi threading is defined as the ability of a processor to execute multiple threads
concurrently. In a simple, single core CPU , it is achieved using frequent between threads.
this is termed context switching...
Context switching: The state of thread is saved and the state of another thread is
loaded whenever any interput(Input/Output) takes place...


whenever we are using multithreading we need import "threading"


'''

import  threading

def squ(num):
    print('square:{}'.format(num**2))
'''
if _name_ == '_main_': #*********************
    t1 = threading.Thread(target=squ, args=(2,))
    t1.start()
    t1.join()
    print('Done')

    Error in _name_ due to new use

'''

'''
aws - EC2, VPC, Subnet, Security groups, SNS, cloud watch logs, ECS, load balancer

DevOps - GIT, Jenkins, Docker commands

Frameworks :. Django, Flask, Aws+lambda's


'''