#include <defs.h>


//-------------------------------------------------------------------------
// Function declarations

__int64 (**init_proc())(void);
__int64 __fastcall sub_400580(); // weak
// int puts(const char *s);
// void setbuf(FILE *stream, char *buf);
// int system(const char *command);
// int printf(const char *format, ...);
// __int64 __fastcall gets(_QWORD); weak
void __fastcall __noreturn start(__int64 a1, __int64 a2, void (*a3)(void));
void *deregister_tm_clones();
__int64 register_tm_clones();
void *_do_global_dtors_aux();
__int64 frame_dummy();
int __cdecl main(int argc, const char **argv, const char **envp);
void _libc_csu_fini(void); // idb
void term_proc();
// int __fastcall _libc_start_main(int (__fastcall *main)(int, char **, char **), int argc, char **ubp_av, void (*init)(void), void (*fini)(void), void (*rtld_fini)(void), void *stack_end);
// __int64 _gmon_start__(void); weak

//-------------------------------------------------------------------------
// Data declarations

_UNKNOWN _libc_csu_init;
__int64 (__fastcall *_frame_dummy_init_array_entry)() = &frame_dummy; // weak
__int64 (__fastcall *_do_global_dtors_aux_fini_array_entry)() = &_do_global_dtors_aux; // weak
__int64 (*qword_602010)(void) = NULL; // weak
char *HEADER = " ______________________________________________________________________\n|^ ^ ^ ^ ^ ^ |L L L L|^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^|\n| ^ ^ ^ ^ ^ ^| L L L | ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ |\n|^ ^ ^ ^ ^ ^ |L L L L|^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ==================^ ^ ^|\n| ^ ^ ^ ^ ^ ^| L L L | ^ ^ ^ ^ ^ ^ ___ ^ ^ ^ ^ /                  \\^ ^ |\n|^ ^_^ ^ ^ ^ =========^ ^ ^ ^ _ ^ /   \\ ^ _ ^ / |                | \\^ ^|\n| ^/_\\^ ^ ^ /_________\\^ ^ ^ /_\\ | //  | /_\\ ^| |   ____  ____   | | ^ |\n|^ =|= ^ =================^ ^=|=^|     |^=|=^ | |  {____}{____}  | |^ ^|\n| ^ ^ ^ ^ |  =========  |^ ^ ^ ^ ^\\___/^ ^ ^ ^| |__%%%%%%%%%%%%__| | ^ |\n|^ ^ ^ ^ ^| /     (   \\ | ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ |/  %%%%%%%%%%%%%%  \\|^ ^|\n.-----. ^ ||     )     ||^ ^.-------.-------.^|  %%%%%%%%%%%%%%%%  | ^ |\n|     |^ ^|| o  ) (  o || ^ |       |       | | /||||||||||||||||\\ |^ ^|\n| ___ | ^ || |  ( )) | ||^ ^| ______|_______|^| |||||||||||||||lc| | ^ |\n|'.____'_^||/!\\@@@@@/!\\|| _'______________.'|==                    =====\n|\\|______|===============|________________|/|\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\n\" ||\"\"\"\"||\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"||\"\"\"\"\"\"\"\"\"\"\"\"\"\"||\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"  \n\"\"''\"\"\"\"''\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"''\"\"\"\"\"\"\"\"\"\"\"\"\"\"''\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\n\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\n\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\""; // idb
_UNKNOWN _bss_start; // weak
FILE *stdout; // idb
FILE *stdin; // idb
FILE *stderr; // idb
char completed_7698; // weak


//----- (0000000000400568) ----------------------------------------------------
__int64 (**init_proc())(void)
{
  __int64 (**result)(void); // rax

  result = &_gmon_start__;
  if ( &_gmon_start__ )
    return (__int64 (**)(void))_gmon_start__();
  return result;
}
// 6020C8: using guessed type __int64 _gmon_start__(void);

//----- (0000000000400580) ----------------------------------------------------
__int64 sub_400580()
{
  return qword_602010();
}
// 400580: using guessed type __int64 __fastcall sub_400580();
// 602010: using guessed type __int64 (*qword_602010)(void);

//----- (00000000004005E0) ----------------------------------------------------
// positive sp value has been detected, the output may be wrong!
void __fastcall __noreturn start(__int64 a1, __int64 a2, void (*a3)(void))
{
  __int64 v3; // rax
  int v4; // esi
  __int64 v5; // [rsp-8h] [rbp-8h] BYREF
  char *retaddr; // [rsp+0h] [rbp+0h] BYREF

  v4 = v5;
  v5 = v3;
  _libc_start_main(
    (int (__fastcall *)(int, char **, char **))main,
    v4,
    &retaddr,
    (void (*)(void))_libc_csu_init,
    _libc_csu_fini,
    a3,
    &v5);
  __halt();
}
// 4005E6: positive sp value 8 has been found
// 4005ED: variable 'v3' is possibly undefined

//----- (0000000000400620) ----------------------------------------------------
void *deregister_tm_clones()
{
  return &_bss_start;
}

//----- (0000000000400650) ----------------------------------------------------
__int64 register_tm_clones()
{
  return 0LL;
}

//----- (0000000000400690) ----------------------------------------------------
void *_do_global_dtors_aux()
{
  void *result; // rax

  if ( !completed_7698 )
  {
    result = deregister_tm_clones();
    completed_7698 = 1;
  }
  return result;
}
// 602088: using guessed type char completed_7698;

//----- (00000000004006C0) ----------------------------------------------------
__int64 frame_dummy()
{
  return register_tm_clones();
}

//----- (00000000004006C7) ----------------------------------------------------
int __cdecl main(int argc, const char **argv, const char **envp)
{
  char v4[264]; // [rsp+0h] [rbp-110h] BYREF
  __int64 v5; // [rsp+108h] [rbp-8h]

  v5 = 0LL;
  setbuf(stdout, 0LL);
  setbuf(stdin, 0LL);
  setbuf(stderr, 0LL);
  puts(HEADER);
  puts("My room is so cluttered...");
  puts("What do you see?");
  gets(v4);
  if ( v5 == 3735928559LL )
  {
    printf("code == 0x%llx: how did that happen??\n", 3735928559LL);
    puts("take a flag for your troubles");
    system("cat flag.txt");
  }
  else
  {
    printf("code == 0x%llx\n", v5);
    printf("code != 0x%llx :(\n", 3735928559LL);
  }
  return 0;
}
// 4005D0: using guessed type __int64 __fastcall gets(_QWORD);
// 4006C7: using guessed type char var_110[264];

//----- (00000000004007D0) ----------------------------------------------------
void __fastcall _libc_csu_init(unsigned int a1, __int64 a2, __int64 a3)
{
  signed __int64 v3; // rbp
  __int64 i; // rbx

  v3 = &_do_global_dtors_aux_fini_array_entry - &_frame_dummy_init_array_entry;
  init_proc();
  if ( v3 )
  {
    for ( i = 0LL; i != v3; ++i )
      (*(&_frame_dummy_init_array_entry + i))();
  }
}
// 601E10: using guessed type __int64 (__fastcall *_frame_dummy_init_array_entry)();
// 601E18: using guessed type __int64 (__fastcall *_do_global_dtors_aux_fini_array_entry)();

//----- (0000000000400844) ----------------------------------------------------
void term_proc()
{
  ;
}