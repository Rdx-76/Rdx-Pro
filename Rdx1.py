

int64_t __gmon_start__ = 0;

void _init() {
    int64_t rax1;

    rax1 = __gmon_start__;
    if (rax1) {
        rax1();
    }
    return;
}

int64_t deregister_tm_clones() {
    int64_t rax1;

    *reinterpret_cast<int32_t*>(&rax1) = 0x602058;
    *reinterpret_cast<int32_t*>(reinterpret_cast<int64_t>(&rax1) + 4) = 0;
    if (1 || (*reinterpret_cast<int32_t*>(&rax1) = 0, *reinterpret_cast<int32_t*>(reinterpret_cast<int64_t>(&rax1) + 4) = 0, 1)) {
        return rax1;
    } else {
        goto 0;
    }
}

int64_t printf = 0x4005c6;

void fun_4005c0(int64_t rdi, int64_t rsi) {
    goto printf;
}

int64_t puts = 0x400596;

void fun_400590(int64_t rdi, int64_t rsi) {
    goto puts;
}

int64_t system = 0x4005b6;

void fun_4005b0(int64_t rdi, int64_t rsi) {
    goto system;
}

int64_t gets = 0x4005d6;

void fun_4005d0(void* rdi, int64_t rsi) {
    goto gets;
}

int64_t setbuf = 0x4005a6;

void fun_4005a0(int64_t rdi, int64_t rsi) {
    goto setbuf;
}

void _fini() {
    return;
}

void fun_400685() {
    int64_t v1;

    goto v1;
}

void fun_4006ab() {
    return;
}

void __libc_csu_fini() {
    return;
}

void fun_40064a() {
    if (1) 
        goto 0x400688;
    if (1) 
        goto 0x400688;
    goto 0;
}

/* completed.7698 */
signed char completed_7698 = 0;

int64_t __do_global_dtors_aux() {
    int1_t zf1;
    int64_t rax2;

    zf1 = completed_7698 == 0;
    if (!zf1) 
        goto 0x4006b0;
    rax2 = deregister_tm_clones();
    completed_7698 = 1;
    return rax2;
}

void frame_dummy() {
    goto 0x400650;
}

int64_t g602010 = 0;

void fun_4005c6() {
    goto g602010;
}

void fun_400596() {
    goto 0x400580;
}

void fun_4005b6() {
    goto 0x400580;
}

void __libc_csu_init(int32_t edi, int64_t rsi, int64_t rdx) {
    int64_t r15_4;
    int32_t r13d5;
    int64_t r14_6;
    int64_t rbx7;
    int64_t rdi8;

    r15_4 = rdx;
    r13d5 = edi;
    r14_6 = rsi;
    _init();
    if (!0) {
        *reinterpret_cast<int32_t*>(&rbx7) = 0;
        *reinterpret_cast<int32_t*>(reinterpret_cast<int64_t>(&rbx7) + 4) = 0;
        do {
            *reinterpret_cast<int32_t*>(&rdi8) = r13d5;
            *reinterpret_cast<int32_t*>(reinterpret_cast<int64_t>(&rdi8) + 4) = 0;
            *reinterpret_cast<int64_t*>(0x601e10 + rbx7 * 8)(rdi8, r14_6, r15_4);
            ++rbx7;
        } while (1 != rbx7);
    }
    return;
}

int64_t stdout = 0;

int64_t stdin = 0;

int64_t stderr = 0;

int64_t HEADER = 0x400858;

int64_t main() {
    int64_t rax1;
    int64_t rax2;
    int64_t rax3;
    int64_t rax4;

    rax1 = stdout;
    fun_4005a0(rax1, 0);
    rax2 = stdin;
    fun_4005a0(rax2, 0);
    rax3 = stderr;
    fun_4005a0(rax3, 0);
    rax4 = HEADER;
    fun_400590(rax4, 0);
    fun_400590("My room is so cluttered...", 0);
    fun_400590("What do you see?", 0);
    fun_4005d0(reinterpret_cast<int64_t>(__zero_stack_offset()) - 8 - 0x110, 0);
    if (1) {
        fun_4005c0("code == 0x%llx\n", 0);
        fun_4005c0("code != 0x%llx :(\n", 0xdeadbeef);
    } else {
        fun_4005c0("code == 0x%llx: how did that happen??\n", 0xdeadbeef);
        fun_400590("take a flag for your troubles", 0xdeadbeef);
        fun_4005b0("cat flag.txt", 0xdeadbeef);
    }
    return 0;
}

void fun_4005d6() {
    goto 0x400580;
}

void fun_4005a6() {
    goto 0x400580;
}

int64_t __libc_start_main = 0;

void _start() {
    void* rsp1;
    int64_t rdx2;
    int64_t rax3;

    rsp1 = reinterpret_cast<void*>(reinterpret_cast<int64_t>(__zero_stack_offset()) + 8);
    __libc_start_main(main, __return_address(), rsp1, __libc_csu_init, __libc_csu_fini, rdx2, (reinterpret_cast<uint64_t>(rsp1) & 0xfffffffffffffff0) - 8 - 8, rax3);
    __asm__("hlt ");
}

void _dl_relocate_static_pie() {
    return;
}















