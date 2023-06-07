# Inverted Index with MapReduce

This project demonstrates the creation of a partial and full inverted index using the MapReduce programming model.

## Concept
An **Inverted Index** is a data structure used to create a full-text search. In a standard index, we map documents to the words they contain. An inverted index flips this relationship around; we map words to the list of documents that contain them.

A **Partial Inverted Index** maps each unique word to the documents that contain the word. On the other hand, a **Full Inverted Index** takes it a step further and also maps each unique word to the index positions of the word in each document.

## Design
- `PartialInvertedIndex.java`: This program takes a list of text files and produces an output file where each line contains a unique word followed by a list of the names of the files in which the word appears.
- `FullInvertedIndex.java`: This program creates a full inverted index. It outputs each unique word followed by a list of the files that contain the word, along with the index positions of the word in each file.

## Running and Testing
1. Compile the Java code into a jar file:
    ```bash
    javac -classpath `${HADOOP_HOME}/bin/hadoop classpath` -d . PartialInvertedIndex.java FullInvertedIndex.java
    jar cf invertedindex.jar *.class
    ```
2. Run the MapReduce job on Hadoop:
    ```bash
    ${HADOOP_HOME}/bin/hadoop jar invertedindex.jar PartialInvertedIndex input-dir partial-index-output-dir
    ${HADOOP_HOME}/bin/hadoop jar invertedindex.jar FullInvertedIndex input-dir full-index-output-dir
    ```
    Replace `input-dir` with the path to the directory containing your input text files, and replace `partial-index-output-dir` and `full-index-output-dir` with the paths to the directories where you want the output files to be written.

3. The output of the programs will be a set of files in the specified output directory. To check the output, you can use the `hdfs dfs -cat` command:
    ```bash
    ${HADOOP_HOME}/bin/hdfs dfs -cat partial-index-output-dir/*
    ${HADOOP_HOME}/bin/hdfs dfs -cat full-index-output-dir/*
    ```
4. To test the programs with different input, you can modify the input text files and rerun the MapReduce jobs. The output should correctly reflect the words and their occurrences in the input files.
