# PDA Simulation with CFG
## Student Information
- **Names:** Samuel Calderon Duque & Matias Monsalve Ruiz.
- **Class Number:** 7309.
## System and Tools 
- **Operating System:** Windows 11 / MacOs Sequoia.
- **Programming Language:** Python 3.13.
- **Tools:** PyCharm 2024.3.3 and we used the random library.
## Instruction
 Have Python installed, open the IDE of your preference, open the files "ALGORITHM_1_LFCO_2025_MS.py", "ALGORITHM_2_LFCO_2025_MS.py" and "ALGORITHM_3_LFCO_2025_MS.py" in the same directory, after that run the files as follows: 
 ```sh 
python ALGORITHM_1_LFCO_2025_MS.py
python ALGORITHM_2_LFCO_2025_MS.py
python ALGORITHM_3_LFCO_2025_MS.py
```
Finally check each algorithm’s output.
## Explanation 
The first algorithm generates both strings that belong to the language defined by the context-free grammar 𝑆→𝑎𝑆𝑏∣𝜖 and strings that do not belong to the language but share the same alphabet (a and b). These strings are saved to a file called strings.txt for use in subsequent algorithms. When you run el ALGORITHM_1_LFCO_2025_MS, the output will show the generated strings and confirm that they have been saved to the file. Example output:

Generated Strings:
  - aaaaabbbbb
  - aabb
  - aaab
  - aaaaabb

The second algorithm processes the strings generated in Algorithm 1 using a Push Down Automaton (PDA). It determines whether each string is accepted or rejected by the grammar. The results are displayed with clear messages indicating the status of each string. When you run ALGORITHM_2_LFCO_2025_MS, the output will show the validation results for all strings.
The string 'aaaaabbbbb' is ACCEPTED by the PDA. Example output:

The string 'aabb' is ACCEPTED by the PDA.

The string 'aaab' is REJECTED by the PDA.

The string 'aaaaabb' is REJECTED by the PDA.

The third algorithm takes the strings validated in Algorithm 2 and displays the derivation process for each string. For strings that are accepted, it shows the steps to derive them using the grammar rules. For strings that are rejected, it performs the same process but ends with a message stating that the derivation could not be completed successfully.
When you run ALGORITHM_3_LFCO_2025_MS, the output will show detailed derivation steps for each string. Example output:

1    S                             aabb
2    aSb                           ab
3    aaSbb                         
4    aaεbb                         End

