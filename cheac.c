#include <stdio.h>

int main() {
  // Open the file in read mode.
  FILE *fp = fopen("database.txt", "r");
  if (fp == NULL) {
    // File does not exist.
    return 1;
  }

  // Read the data from the file.
  char name[100];
  int age;
  while (fscanf(fp, "%s %d", name, &age) != EOF) {
    // Print the data to the console.
    printf("%s %d\n", name, age);
  }

  // Close the file.
  fclose(fp);

  return 0;
}