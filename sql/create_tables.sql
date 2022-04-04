drop table postal_codes;
/* table creation */
CREATE TABLE postal_codes ( 
    the_geom geometry,
    code VARCHAR(5),
    id INTEGER PRIMARY KEY

);


CREATE TABLE payment_stats (
    amount FLOAT,
    p_month VARCHAR(10),
    p_age VARCHAR(6),
    p_gender VARCHAR(1),
    postal_code_id VARCHAR(5),
    id integer
);
/* example to create a polygon */
insert into postal_codes values ('0103000020E61000000100000042000000FE76287E0CAE0EC0DFB024C5CB324440FF8D17AEC1AF0EC09607B648C7324440FEE4F15D63B20EC00FDCA5CEC43244407D2B422689B50EC0D781D23CCC324440FD3B81BDB3BB0EC08E040CCED73244407DB6930BE2BB0EC097247E41D13244407F7876A5F1BB0EC006929208CF324440FE4388E8E4BC0EC0F608147BA63244407D65E426EABC0EC02FCC1CF1A53244407E724CD057C30EC08FA39D2DDD324440FDEE8A2EDECD0EC07E40389D373344407E1FE13437C80EC0D7078EBB3A334440FF84B4FAE6C40EC0B74A2E1A793344407E2C95239EC70EC0FF6D486BCA3344407E758DEB07CD0EC0A761F2A9173444407E56043C5BD10EC04E11788744344440FFD9D4CF27D50EC01FEAE1BD6E3444407F667236CBD70EC0A70F38B184344440FE24E113D1DA0EC086B3397BB6344440FEA0F4C161DB0EC027B730CABF344440FECEE89853DA0EC0FF87BBEBC93444407DAF6671BAD20EC0EE56A882F7344440FD8636DB47C80EC02FD1C947193544407D736DAC48C20EC00753056B5D354440FEBE820E6AC00EC0C70AC38B5C3544407E0A589D81BE0EC04E428E657D354440FF568D6074BE0EC05731034A7E354440FF2EABA10BBD0EC06E89B48C963544407E624B13F7BC0EC0178CBDEE97354440FD83F1AFA6BC0EC05F5FF0BC803544407EC8820E83BC0EC0FE8854D8773544407E87DD5647BC0EC08F860B3C65354440FF43098431BC0EC0CF1AAED15B3544407D851A282CBC0EC0F6133581593544407DCC1631F8BB0EC09FCB870F43354440FD0201BEBCBB0EC0EF3A6F66293544407DE73416ABBB0EC00619FAC01F3544407E8357465ABB0EC0271FB899F3344440FE033F4109BB0EC0DF5B970BCB3444407E20219737BA0EC00FA5487F7C3444407D5947007DB80EC09F13F9741B3444407E1825FDD7B30EC02F05BC9C94334440FE69BE01DAAF0EC0EFACD08A843344407E96D4486FAD0EC016650DF6783344407F4B7B5A61AD0EC0D7556CB378334440FD48804322A80EC02636E48E5F334440FE1AB51D53A70EC0B7F6DE085D334440FE939A4909A70EC0BFB2B1225C3344407D00BDA4CCA50EC0EF4A284858334440FFA00B5EA7A50EC0D7A6C0D3573344407E02540CA7A50EC0EEE5D8D257334440FECEEADC88A50EC0AEF7517457334440FD0B70E687A50EC0472E5571573344407ECBFEAF70A80EC077A4F72B30334440FE102A122CA80EC0AE2658472D334440FE0F925E2CA80EC097640C422D334440FFA1AA232CA80EC0C673A03F2D334440FF490E380FAA0EC0B68BC0970D334440FE3311A919AA0EC01FEB48E80C3344407EF60EEC19AA0EC00F9899E30C334440FFA82C0E27AA0EC0EEE607FD0B334440FE31339D0AAC0EC0FF2FB254EC324440FFFE443CC8AC0EC0D70266D8DF324440FF636C18E0AC0EC04F3CAA6DDE324440FF316658F0AC0EC01781536BDD324440FE76287E0CAE0EC0DFB024C5CB324440','28005',1);

/* import the postal_codes into the table using copy */
\copy payment_stats (ammount,p_month,p_age,p_gender,postal_code_id,id) from 'payment_stats.csv' (format csv, header, delimiter ',')

\copy postal_codes (the_geom,code,id) from 'postal_codes.csv' (format csv, header, delimiter ',')