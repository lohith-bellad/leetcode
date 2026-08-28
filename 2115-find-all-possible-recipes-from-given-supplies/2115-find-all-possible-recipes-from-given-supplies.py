class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        def dfs(item, taken):
            if item in taken:
                return False

            if item not in mapping:
                return False
            
            if item in output:
                return True

            taken.add(item)

            for needed in mapping[item]:
                if not dfs(needed, taken):
                    return False
            
            taken.remove(item)
            
            return True

        mapping = {}
        n = len(recipes)
        output = []

        for i in range(n):
            mapping[recipes[i]] = ingredients[i]
            for ing in ingredients[i]:
                if ing in supplies:
                    mapping[ing] = []
        
        for recipe in recipes:
            if dfs(recipe, set()):
                output.append(recipe)

        return output