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
        
    </body>
</html>