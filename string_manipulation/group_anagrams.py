def group_anagrams(self, strs: List[str]) ->List[List[str]]:
    anagrams = collections.defauldict(list)

    for word in strs:
        anagrams[''.join(sorted(word))].append(word)
    return anagrams.values()