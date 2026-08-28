class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        def dfs(item):
            if item in taken:
                return False

            if item not in mapping:
                return False
            
            if item in cache:
                return True

            taken.add(item)

            for needed in mapping[item]:
                if not dfs(needed):
                    return False
            
            taken.remove(item)
            
            return True

        mapping = {}
        n = len(recipes)

        for i in range(n):
            mapping[recipes[i]] = ingredients[i]

        for s in supplies:
            mapping[s] = []

        cache = {}
        output = []
        taken = set()
        for recipe in recipes:
            if dfs(recipe):
                output.append(recipe)

        return output