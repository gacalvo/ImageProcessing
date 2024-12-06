%wrapper rule main
main:-
    read(Input),
    reverse_list(Input, Reversed),
    write(Reversed).

%reverse the list
%base case; empty list
reverse_list([],[]).
%recursive case
reverse_list([Input|Inputs], Result):-
    %recursive call on tail
    reverse_list(Inputs, Reversed),
    %append new list list to head
    append(Reversed, [Input], Result).

write_list([]).
write_list(X|Xs):-
    write([X]),
    write_list(Xs).
