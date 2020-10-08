#include <stdio.h>
#include <stdlib.h>     // exit
#include <stdint.h>
#include <unistd.h>     // usleep
//#include <sys/stat.h>
//#include <sys/types.h>
#include <fcntl.h>      // open
#include <sys/mman.h>   // mmap

uint32_t *map_gpio()
{
    char *fname = "/dev/gpiomem";
    int fd = open(fname, O_RDWR | O_SYNC, 0666);
    if (fd < 0) {
        perror(fname);
        exit(EXIT_FAILURE);
    }
    uint32_t *base = mmap(
        NULL,
        180,
        PROT_READ | PROT_WRITE,
        MAP_SHARED,
        fd,
        0
    );
    close(fd);
    return base;
}

uint32_t *gpio_base;

int main()
{
    gpio_base = map_gpio();

    printf("GPIO registers\n");
    for (int i = 0; i < 16; i++) {
        printf("%02x %08x\n", 4*i, gpio_base[i]);
    }

    printf("blinking LED connected to gpio 6...\n");
    for (int i = 0; i < 4; i++) {
        gpio_base[7] = 0x40;  //set gpio 6
        usleep(500000);
        gpio_base[10] = 0x40; //clr gpio 6
        usleep(500000);
    }
    return 0;
}
