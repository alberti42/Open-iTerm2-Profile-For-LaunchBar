// OpenITerm2Profile — the executable of Open iTerm2 Profile.lbaction.
//
// LaunchBar does not run this program; it runs the scripts in
// Contents/Scripts. The program exists so that the bundle has Mach-O code:
// signing the bundle embeds the signature, which seals the scripts, in this
// executable, and
// Apple's notary service issues tickets only for Mach-O code. Without it,
// Gatekeeper rejects the downloaded action ("Apple could not verify ... is
// free of malware").

#include <stdio.h>

int main(void)
{
    fputs("Open iTerm2 Profile: LaunchBar runs the scripts in Contents/Scripts; "
          "this program does nothing.\n", stderr);
    return 0;
}
