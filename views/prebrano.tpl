<html>
    <body>

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