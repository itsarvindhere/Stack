def simplifyPath(path: str) -> str:
	# Slashes are the main part of the path
        # Each part of path is enclosed within slashes
        # So, we will first split our path at slashes
        path = path.split("/")
        
        # Stack that we will use to construct our final path
        stack = [""]
        
        # Length of the path (after splitting)
        n = len(path)
        
        i = 0
        while i < n: 
            
            # If we get a single dot
            if path[i] == ".":
                i += 1
                continue
            
            # If we have double dots,it means go one level up
            if path[i] == "..":
                # We only go one level up if we are not already in root directory
                if len(stack) != 1: stack.pop()     
                    
            # If we get name of file or folder, push it to stack
            elif path[i] != "": stack.append(path[i])

            i += 1
              
        return "/" if len(stack) == 1 else "/".join(stack)


path = "/a/./b/../../c/"

print("Simplified Path -> ", simplifyPath(path))