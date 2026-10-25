#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

#define BLOCK_SIZE 512

int main(int argc, char *argv[])
{
    // Ensure proper usage
    if (argc != 2)
    {
        printf("Usage: ./recover IMAGE\n");
        return 1;
    }

    // Open memory card file
    FILE *input_file = fopen(argv[1], "r");
    if (input_file == NULL)
    {
        printf("Could not open file: %s\n", argv[1]);
        return 1;
    }

    // Buffer to store a block of data
    uint8_t buffer[BLOCK_SIZE];

    // File pointer for recovered images
    FILE *output_file = NULL;

    // Char array to store the filename (e.g., "000.jpg")
    char filename[8];

    // Counter for found images
    int image_count = 0;

    // Read blocks from the memory card until the end of the file
    while (fread(buffer, 1, BLOCK_SIZE, input_file) == BLOCK_SIZE)
    {
        // Check if block is the beginning of a JPEG
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            // If already writing an image, close the previous one
            if (output_file != NULL)
            {
                fclose(output_file);
            }

            // Create filename for new JPEG
            sprintf(filename, "%03i.jpg", image_count);

            // Open new JPEG file for writing
            output_file = fopen(filename, "w");
            if (output_file == NULL)
            {
                fclose(input_file);
                printf("Could not create output file %s\n", filename);
                return 1;
            }

            image_count++;
        }

        // If we have found a JPEG, write the block to the output file
        if (output_file != NULL)
        {
            fwrite(buffer, 1, BLOCK_SIZE, output_file);
        }
    }

    // Close any remaining open files
    if (output_file != NULL)
    {
        fclose(output_file);
    }

    fclose(input_file);
    return 0;
}
