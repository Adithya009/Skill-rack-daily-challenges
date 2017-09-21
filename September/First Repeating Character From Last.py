import sys
s=raw_input().strip()
for i in range(len(s)-1,-1,-1):
    for j in range(i-1,-1,-1):
        if s[i]==s[j]:
            print s[i];
            sys.exit()
    
