<html>
    <body>
        <h1>Seznam zelja</h1>
        <h2>Seznam knjig, ki jih želim prebrati</h2>

        % if st_knjig_sez_zelja == 0:
        <h3>Na seznamu želja nimate nobene knjige!</h3>
        % elif st_knjig_sez_zelja == 1:
        <h3>Na seznamu želja imate {{st_knjig_sez_zelja}} knjigo!</h3>
        % elif st_knjig_sez_zelja == 2:
        <h3>Na seznamu želja imate {{st_knjig_sez_zelja}} knjigi!</h3>
        % elif 3 <= st_knjig_sez_zelja <= 4:
        <h3>Na seznamu želja imate {{st_knjig_sez_zelja}} knjige!</h3>
        % else:
        <h3>Na seznamu želja imate {{st_knjig_sez_zelja}} knjig!</h3>
        %end

        <ul>
        %for knjiga in knjige_sez_zelja:
        <li>{{knjiga}}</li>
        %end
        </ul>

        <form action="/dodaj/>
            naslov: <input type="text "name="naslov">
            avtor: <input type="text "name="avtor">
            število strani: <input type="number "name="st_strani">
            <input type="submit" value="dodaj knjigo">
        </form>

        <h1>Prebrano</h1>
        
        <h2>Seznam že prebranih knjig.</h2>
        
        % if st_knjig_prebrano == 0:
        <h3>Prebrali niste še nobene knjige!</h3>
        % elif st_knjig_prebrano == 1:
        <h3>Prebrali ste {{st_knjig_prebrano}} knjigo.</h3>
        % elif st_knjig_prebrano == 2:
        <h3>Prebrali ste {{st_knjig_prebrano}} knjigi.</h3>
        % elif 3 <= st_knjig_prebrano <= 4:
        <h3>Prebrali ste {{st_knjig_prebrano}} knjige.</h3>
        % else:
        <h3>Prebrali ste {{st_knjig_prebrano}} knjig.</h3>
        %end

        <ul>
        %for knjiga in prebrane_knjige:
        <li>{{knjiga}}</li>
        %end
        </ul>



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


        <h1>Prebrano</h1>
        <h2>Seznam že prebranih knjig.</h2>
        
        % if st_knjig_prebrano == 0:
        <h3>Prebrali niste še nobene knjige!</h3>
        % elif st_knjig_prebrano == 1:
        <h3>Prebrali ste {{st_knjig_prebrano}} knjigo.</h3>
        % elif st_knjig_prebrano == 2:
        <h3>Prebrali ste {{st_knjig_prebrano}} knjigi.</h3>
        % elif 3 <= st_knjig_prebrano <= 4:
        <h3>Prebrali ste {{st_knjig_prebrano}} knjige.</h3>
        % else:
        <h3>Prebrali ste {{st_knjig_prebrano}} knjig.</h3>
        %end

        <ul>
        %for knjiga in prebrane_knjige:
        <li>{{knjiga}}</li>
        %end
        </ul>


    </body>
</html>