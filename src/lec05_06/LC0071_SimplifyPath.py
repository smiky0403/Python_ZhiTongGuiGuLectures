def simplifyPath(self, path: str) -> str:
    st1 = list()
    for s in path.split('/'):
        if s == "..":
            if len(st1) > 0:
                st1.pop()
        elif s == "." or s == "":
            continue
        else:
            st1.append(s)

        print(st1)
    
    return "/" + "/".join(st1)



def main():
    path = "/.../a/../b//c/../d/./"
    for s in path.split('/'):
        print(s)
        
    print(simplifyPath(path))

    
main()