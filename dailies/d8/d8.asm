BITS 16

;	Matthew Phelps 

start:
                ; here's our prelude of setting up the data and stack sections
                ; this is the prelude, where we set up the data
                ; and stack segments
cli             ; turn off interrupts while setting up DS and SS
mov ax, 07C0h   ; recall that 07C0h is where the bootloader starts
                ; so, that is the start of the data segment (DS)
mov ds, ax      ; move AX into DS because we can't set DS directly
                ; that's all we need to do for the data segment...
                ; ...now we need to set up the stack
                ; to do that, we move forward by 512 bytes (the
                ; size of this bootloader) to get a starting point
                ; for the stack.
                ; to do that, we want the stack segment (SS register)
                ; to point to the end of the bootloader, which is
                ; the data segment start (07C0h) plus the size of the
                ; the bootloader.
                ; but, segments are addressed in multiples of 16
                ; (called "paragraphs"), so we actually add 512/16=
add ax, 0020h   ; 32, which is 0020 in hex
mov ss, ax      ; set the stack segment to 07E0h (07C0h + 0020h)
mov sp, 1000h   ; set the stack pointer to 4096 bytes (1000h)
                ; remember that this will grow *down*, towards SS
sti             ; turn the interrupts back on
cld             ; clear direction flag for lodsb, end of prelude

call print      ; -- Call procedure print defined below ...
jmp $           ; loop until the power goes out

print: ; start of procedure print
mov ah, 0Eh ; -- specify teletype output
mov al, 43h ; -- set character to print ('C' is 43 in hex)
mov bh, 0h ; -- set the video page number
mov bl, 04h ; -- color setting
int 10h ; -- interrupt and write the character al on the screen and move cursor one position
ret ; end of procedure print

times 510-($-$$) db 0	; fill remainder of sector with zeros
dw 0xAA55		; BIOS looks for AA55 at the end of the sector

