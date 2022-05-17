from MiniAssignment1.EqualSumPairs import EqualSumPairs
from MiniAssignment1.PairsPossible import PairsPossible
from MiniAssignment1.SearchCommonElements import SearchCommonElements

if __name__ == '__main__':
    pairs_possible = PairsPossible()
    pairs_possible.all_possible_pairs()
    pairs_possible.print_pairs()

    search_common_elements = SearchCommonElements()
    search_common_elements.common_elements(pairs_possible.convert_into_list_char(pairs_possible.get_str()))

    equal_sum_pairs = EqualSumPairs()
    equal_sum_pairs.count_pair_with_distinct_sum(pairs_possible)

    search_common_elements.print_common_elements()
    equal_sum_pairs.print_count()

