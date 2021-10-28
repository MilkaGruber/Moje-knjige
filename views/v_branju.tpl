<html>
    <body>
        <h1>V branju</h1>

        <h2>Seznam knjig, ki jih trenutno berete.</h2>

        % if  st_knjig_v_branju == 0:
        <h3>Trentno ne berete nobene knjige!</h3>
        % elif  st_knjig_v_branju == 1:
        <h3>Trentno berete {{st_knjig_v_branju}} knjigo!</h3>
        % elif  st_knjig_v_branju == 2:
        <h3>Trentno berete {{st_knjig_v_branju}} knjigi!</h3>
        % elif 3 <=  st_knjig_v_branju <= 4:
        <h3>Trentno berete {{st_knjig_v_branju}} knjige!</h3>
        % else:
        <h3>Trentno berete {{st_knjig_v_branju}} knjig!</h3>
        %end

        <ul>
        %for knjiga in knjige_v_branju:
        <li>{{knjiga}}</li>
        %end
        </ul>

    </body>
</html>