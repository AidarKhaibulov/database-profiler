-- Prepare data
DROP SEQUENCE IF EXISTS song_sequence;
DROP TABLE IF EXISTS songs cascade;
DROP SEQUENCE IF EXISTS band_sequence;
DROP TABLE IF EXISTS bands cascade;

create sequence band_sequence start with 1 increment by 1;
CREATE TABLE bands (
	id bigint primary key,
	name varchar(255) NULL,
	genre varchar(255) NULL
);

create sequence song_sequence start with 1 increment by 1;
CREATE TABLE songs (
	id bigint NOT NULL,
	duration_in_seconds int4 NULL,
	lyrics text NULL,
	title varchar(255) NULL,
	band_id bigint not null
	constraint fk_song_band references bands on delete cascade
);

-- Initial data set up
INSERT INTO bands (id,name, genre) VALUES
    (nextval('band_sequence'),'Black Sabbath', 'Heavy Metal'),
    (nextval('band_sequence'),'Iron Maiden', 'Heavy Metal'),
    (nextval('band_sequence'),'Death', 'Death Metal'),
    (nextval('band_sequence'),'Slayer', 'Thrash Metal'),
    (nextval('band_sequence'),'Kreator', 'Thrash Metal'),
    (nextval('band_sequence'),'Sepultura', 'Thrash Metal'),
    (nextval('band_sequence'),'Dio', 'Heavy Metal'),
    (nextval('band_sequence'),'W.A.S.P.', 'Heavy Metal'),
    (nextval('band_sequence'),'Carcass', 'Death Metal'),
    (nextval('band_sequence'),'Amon Amarth', 'Melodic Death Metal');

INSERT INTO songs (id, duration_in_seconds, lyrics, title, band_id) VALUES
    (nextval('song_sequence'), 300, 'Текст песни для Paranoid', 'Paranoid', (SELECT id FROM bands WHERE name = 'Black Sabbath')),
    (nextval('song_sequence'), 240, 'Текст песни для Iron Man', 'Iron Man', (SELECT id FROM bands WHERE name = 'Black Sabbath')),
    (nextval('song_sequence'), 330, 'Текст песни для War Pigs', 'War Pigs', (SELECT id FROM bands WHERE name = 'Black Sabbath')),
    (nextval('song_sequence'), 280, 'Текст песни для Sabbath Bloody Sabbath', 'Sabbath Bloody Sabbath', (SELECT id FROM bands WHERE name = 'Black Sabbath')),
    (nextval('song_sequence'), 320, 'Текст песни для Children of the Grave', 'Children of the Grave', (SELECT id FROM bands WHERE name = 'Black Sabbath')),
    (nextval('song_sequence'), 260, 'Текст песни для N.I.B.', 'N.I.B.', (SELECT id FROM bands WHERE name = 'Black Sabbath')),
    (nextval('song_sequence'), 300, 'Текст песни для Sweet Leaf', 'Sweet Leaf', (SELECT id FROM bands WHERE name = 'Black Sabbath')),
    (nextval('song_sequence'), 310, 'Текст песни для Heaven and Hell', 'Heaven and Hell', (SELECT id FROM bands WHERE name = 'Black Sabbath')),
    (nextval('song_sequence'), 270, 'Текст песни для Changes', 'Changes', (SELECT id FROM bands WHERE name = 'Black Sabbath')),
    (nextval('song_sequence'), 290, 'Текст песни для The Wizard', 'The Wizard', (SELECT id FROM bands WHERE name = 'Black Sabbath'));

INSERT INTO songs (id, duration_in_seconds, lyrics, title, band_id) VALUES
    (nextval('song_sequence'), 300, 'Текст песни для Run to the Hills', 'Run to the Hills', (SELECT id FROM bands WHERE name = 'Iron Maiden')),
    (nextval('song_sequence'), 240, 'Текст песни для The Number of the Beast', 'The Number of the Beast', (SELECT id FROM bands WHERE name = 'Iron Maiden')),
    (nextval('song_sequence'), 330, 'Текст песни для Hallowed Be Thy Name', 'Hallowed Be Thy Name', (SELECT id FROM bands WHERE name = 'Iron Maiden')),
    (nextval('song_sequence'), 280, 'Текст песни для Fear of the Dark', 'Fear of the Dark', (SELECT id FROM bands WHERE name = 'Iron Maiden')),
    (nextval('song_sequence'), 320, 'Текст песни для Trooper', 'The Trooper', (SELECT id FROM bands WHERE name = 'Iron Maiden')),
    (nextval('song_sequence'), 260, 'Текст песни для Wasted Years', 'Wasted Years', (SELECT id FROM bands WHERE name = 'Iron Maiden')),
    (nextval('song_sequence'), 300, 'Текст песни для Aces High', 'Aces High', (SELECT id FROM bands WHERE name = 'Iron Maiden')),
    (nextval('song_sequence'), 310, 'Текст песни для Powerslave', 'Powerslave', (SELECT id FROM bands WHERE name = 'Iron Maiden')),
    (nextval('song_sequence'), 270, 'Текст песни для Phantom of the Opera', 'Phantom of the Opera', (SELECT id FROM bands WHERE name = 'Iron Maiden')),
    (nextval('song_sequence'), 290, 'Текст песни для Two Minutes to Midnight', 'Two Minutes to Midnight', (SELECT id FROM bands WHERE name = 'Iron Maiden'));

INSERT INTO songs (id, duration_in_seconds, lyrics, title, band_id) VALUES
    (nextval('song_sequence'), 300, 'Текст песни для Crystal Mountain', 'Crystal Mountain', (SELECT id FROM bands WHERE name = 'Death')),
    (nextval('song_sequence'), 240, 'Текст песни для Symbolic', 'Symbolic', (SELECT id FROM bands WHERE name = 'Death')),
    (nextval('song_sequence'), 330, 'Текст песни для The Philosopher', 'The Philosopher', (SELECT id FROM bands WHERE name = 'Death')),
    (nextval('song_sequence'), 280, 'Текст песни для Pull the Plug', 'Pull the Plug', (SELECT id FROM bands WHERE name = 'Death')),
    (nextval('song_sequence'), 320, 'Текст песни для Lack of Comprehension', 'Lack of Comprehension', (SELECT id FROM bands WHERE name = 'Death')),
    (nextval('song_sequence'), 260, 'Текст песни для Zombie Ritual', 'Zombie Ritual', (SELECT id FROM bands WHERE name = 'Death')),
    (nextval('song_sequence'), 300, 'Текст песни для Flesh and the Power It Holds', 'Flesh and the Power It Holds', (SELECT id FROM bands WHERE name = 'Death')),
    (nextval('song_sequence'), 310, 'Текст песни для Crystal Clear', 'Crystal Clear', (SELECT id FROM bands WHERE name = 'Death')),
    (nextval('song_sequence'), 270, 'Текст песни для Spirit Crusher', 'Spirit Crusher', (SELECT id FROM bands WHERE name = 'Death')),
    (nextval('song_sequence'), 290, 'Текст песни для Voice of the Soul', 'Voice of the Soul', (SELECT id FROM bands WHERE name = 'Death'));

INSERT INTO songs (id, duration_in_seconds, lyrics, title, band_id) VALUES
    (nextval('song_sequence'), 300, 'Текст песни для Angel of Death', 'Angel of Death', (SELECT id FROM bands WHERE name = 'Slayer')),
    (nextval('song_sequence'), 240, 'Текст песни для Raining Blood', 'Raining Blood', (SELECT id FROM bands WHERE name = 'Slayer')),
    (nextval('song_sequence'), 330, 'Текст песни для South of Heaven', 'South of Heaven', (SELECT id FROM bands WHERE name = 'Slayer')),
    (nextval('song_sequence'), 280, 'Текст песни для Seasons in the Abyss', 'Seasons in the Abyss', (SELECT id FROM bands WHERE name = 'Slayer')),
    (nextval('song_sequence'), 320, 'Текст песни для War Ensemble', 'War Ensemble', (SELECT id FROM bands WHERE name = 'Slayer')),
    (nextval('song_sequence'), 260, 'Текст песни для Dead Skin Mask', 'Dead Skin Mask', (SELECT id FROM bands WHERE name = 'Slayer')),
    (nextval('song_sequence'), 300, 'Текст песни для Disciple', 'Disciple', (SELECT id FROM bands WHERE name = 'Slayer')),
    (nextval('song_sequence'), 310, 'Текст песни для Mandatory Suicide', 'Mandatory Suicide', (SELECT id FROM bands WHERE name = 'Slayer')),
    (nextval('song_sequence'), 270, 'Текст песни для Repentless', 'Repentless', (SELECT id FROM bands WHERE name = 'Slayer')),
    (nextval('song_sequence'), 290, 'Текст песни для Black Magic', 'Black Magic', (SELECT id FROM bands WHERE name = 'Slayer'));

INSERT INTO songs (id, duration_in_seconds, lyrics, title, band_id) VALUES
    (nextval('song_sequence'), 300, 'Текст песни для Pleasure to Kill', 'Pleasure to Kill', (SELECT id FROM bands WHERE name = 'Kreator')),
    (nextval('song_sequence'), 240, 'Текст песни для Hordes of Chaos', 'Hordes of Chaos', (SELECT id FROM bands WHERE name = 'Kreator')),
    (nextval('song_sequence'), 330, 'Текст песни для Enemy of God', 'Enemy of God', (SELECT id FROM bands WHERE name = 'Kreator')),
    (nextval('song_sequence'), 280, 'Текст песни для Violent Revolution', 'Violent Revolution', (SELECT id FROM bands WHERE name = 'Kreator')),
    (nextval('song_sequence'), 320, 'Текст песни для Phantom Antichrist', 'Phantom Antichrist', (SELECT id FROM bands WHERE name = 'Kreator')),
    (nextval('song_sequence'), 260, 'Текст песни для Gods of Violence', 'Gods of Violence', (SELECT id FROM bands WHERE name = 'Kreator')),
    (nextval('song_sequence'), 300, 'Текст песни для Endless Pain', 'Endless Pain', (SELECT id FROM bands WHERE name = 'Kreator')),
    (nextval('song_sequence'), 310, 'Текст песни для Extreme Aggression', 'Extreme Aggression', (SELECT id FROM bands WHERE name = 'Kreator')),
    (nextval('song_sequence'), 270, 'Текст песни для Betrayer', 'Betrayer', (SELECT id FROM bands WHERE name = 'Kreator')),
    (nextval('song_sequence'), 290, 'Текст песни для Civilization Collapse', 'Civilization Collapse', (SELECT id FROM bands WHERE name = 'Kreator'));

INSERT INTO songs (id, duration_in_seconds, lyrics, title, band_id) VALUES
    (nextval('song_sequence'), 300, 'Текст песни для Roots Bloody Roots', 'Roots Bloody Roots', (SELECT id FROM bands WHERE name = 'Sepultura')),
    (nextval('song_sequence'), 240, 'Текст песни для Arise', 'Arise', (SELECT id FROM bands WHERE name = 'Sepultura')),
    (nextval('song_sequence'), 330, 'Текст песни для Refuse/Resist', 'Refuse/Resist', (SELECT id FROM bands WHERE name = 'Sepultura')),
    (nextval('song_sequence'), 280, 'Текст песни для Territory', 'Territory', (SELECT id FROM bands WHERE name = 'Sepultura')),
    (nextval('song_sequence'), 320, 'Текст песни для Inner Self', 'Inner Self', (SELECT id FROM bands WHERE name = 'Sepultura')),
    (nextval('song_sequence'), 260, 'Текст песни для Chaos A.D.', 'Chaos A.D.', (SELECT id FROM bands WHERE name = 'Sepultura')),
    (nextval('song_sequence'), 300, 'Текст песни для Slave New World', 'Slave New World', (SELECT id FROM bands WHERE name = 'Sepultura')),
    (nextval('song_sequence'), 310, 'Текст песни для Ratamahatta', 'Ratamahatta', (SELECT id FROM bands WHERE name = 'Sepultura')),
    (nextval('song_sequence'), 270, 'Текст песни для Desperate Cry', 'Desperate Cry', (SELECT id FROM bands WHERE name = 'Sepultura')),
    (nextval('song_sequence'), 290, 'Текст песни для Attitude', 'Attitude', (SELECT id FROM bands WHERE name = 'Sepultura'));

INSERT INTO songs (id, duration_in_seconds, lyrics, title, band_id) VALUES
    (nextval('song_sequence'), 300, E'Текст песни для Holy Diver', 'Holy Diver', (SELECT id FROM bands WHERE name = 'Dio')),
    (nextval('song_sequence'), 240, E'Текст песни для Rainbow in the Dark', 'Rainbow in the Dark', (SELECT id FROM bands WHERE name = 'Dio')),
    (nextval('song_sequence'), 330, E'Текст песни для The Last in Line', 'The Last in Line', (SELECT id FROM bands WHERE name = 'Dio')),
    (nextval('song_sequence'), 280, E'Текст песни для Heaven and Hell', 'Heaven and Hell', (SELECT id FROM bands WHERE name = 'Dio')),
    (nextval('song_sequence'), 320, E'Текст песни для Stand Up and Shout', 'Stand Up and Shout', (SELECT id FROM bands WHERE name = 'Dio')),
    (nextval('song_sequence'), 260, E'Текст песни для Don''t Talk to Strangers', 'Don''t Talk to Strangers', (SELECT id FROM bands WHERE name = 'Dio')),
    (nextval('song_sequence'), 300, E'Текст песни для We Rock', 'We Rock', (SELECT id FROM bands WHERE name = 'Dio')),
    (nextval('song_sequence'), 310, E'Текст песни для Neon Knights', 'Neon Knights', (SELECT id FROM bands WHERE name = 'Dio')),
    (nextval('song_sequence'), 270, E'Текст песни для Invisible', 'Invisible', (SELECT id FROM bands WHERE name = 'Dio')),
    (nextval('song_sequence'), 290, E'Текст песни для All the Fools Sailed Away', 'All the Fools Sailed Away', (SELECT id FROM bands WHERE name = 'Dio'));

INSERT INTO songs (id, duration_in_seconds, lyrics, title, band_id) VALUES
    (nextval('song_sequence'), 300, E'Текст песни для Wild Child', 'Wild Child', (SELECT id FROM bands WHERE name = 'W.A.S.P.')),
    (nextval('song_sequence'), 240, E'Текст песни для I Wanna Be Somebody', 'I Wanna Be Somebody', (SELECT id FROM bands WHERE name = 'W.A.S.P.')),
    (nextval('song_sequence'), 330, E'Текст песни для Blind in Texas', 'Blind in Texas', (SELECT id FROM bands WHERE name = 'W.A.S.P.')),
    (nextval('song_sequence'), 280, E'Текст песни для Animal', 'Animal', (SELECT id FROM bands WHERE name = 'W.A.S.P.')),
    (nextval('song_sequence'), 320, E'Текст песни для The Headless Children', 'The Headless Children', (SELECT id FROM bands WHERE name = 'W.A.S.P.')),
    (nextval('song_sequence'), 260, E'Текст песни для L.O.V.E. Machine', 'L.O.V.E. Machine', (SELECT id FROM bands WHERE name = 'W.A.S.P.')),
    (nextval('song_sequence'), 300, E'Текст песни для Chainsaw Charlie (Murders in the New Morgue)', 'Chainsaw Charlie (Murders in the New Morgue)', (SELECT id FROM bands WHERE name = 'W.A.S.P.')),
    (nextval('song_sequence'), 310, E'Текст песни для Hold On to My Heart', 'Hold On to My Heart', (SELECT id FROM bands WHERE name = 'W.A.S.P.')),
    (nextval('song_sequence'), 270, E'Текст песни для Forever Free', 'Forever Free', (SELECT id FROM bands WHERE name = 'W.A.S.P.')),
    (nextval('song_sequence'), 290, E'Текст песни для Heaven\'s Hung in Black', E'Heaven\'s Hung in Black', (SELECT id FROM bands WHERE name = 'W.A.S.P.'));

INSERT INTO songs (id, duration_in_seconds, lyrics, title, band_id) VALUES
    (nextval('song_sequence'), 300, E'Текст песни для Heartwork', 'Heartwork', (SELECT id FROM bands WHERE name = 'Carcass')),
    (nextval('song_sequence'), 240, E'Текст песни для Corporal Jigsore Quandary', 'Corporal Jigsore Quandary', (SELECT id FROM bands WHERE name = 'Carcass')),
    (nextval('song_sequence'), 330, E'Текст песни для No Love Lost', 'No Love Lost', (SELECT id FROM bands WHERE name = 'Carcass')),
    (nextval('song_sequence'), 280, E'Текст песни для Buried Dreams', 'Buried Dreams', (SELECT id FROM bands WHERE name = 'Carcass')),
    (nextval('song_sequence'), 320, E'Текст песни для Keep on Rotting in the Free World', 'Keep on Rotting in the Free World', (SELECT id FROM bands WHERE name = 'Carcass')),
    (nextval('song_sequence'), 260, E'Текст песни для Reek of Putrefaction', 'Reek of Putrefaction', (SELECT id FROM bands WHERE name = 'Carcass')),
    (nextval('song_sequence'), 300, E'Текст песни для Exhume to Consume', 'Exhume to Consume', (SELECT id FROM bands WHERE name = 'Carcass')),
    (nextval('song_sequence'), 310, E'Текст песни для This Mortal Coil', 'This Mortal Coil', (SELECT id FROM bands WHERE name = 'Carcass')),
    (nextval('song_sequence'), 270, E'Текст песни для Black Star', 'Black Star', (SELECT id FROM bands WHERE name = 'Carcass')),
    (nextval('song_sequence'), 290, E'Текст песни для Symposium of Sickness', 'Symposium of Sickness', (SELECT id FROM bands WHERE name = 'Carcass'));

INSERT INTO songs (id, duration_in_seconds, lyrics, title, band_id) VALUES
    (nextval('song_sequence'), 300, E'Текст песни для Twilight of the Thunder God', 'Twilight of the Thunder God', (SELECT id FROM bands WHERE name = 'Amon Amarth')),
    (nextval('song_sequence'), 240, E'Текст песни для Guardians of Asgaard', 'Guardians of Asgaard', (SELECT id FROM bands WHERE name = 'Amon Amarth')),
    (nextval('song_sequence'), 330, E'Текст песни для Pursuit of Vikings', 'Pursuit of Vikings', (SELECT id FROM bands WHERE name = 'Amon Amarth')),
    (nextval('song_sequence'), 280, E'Текст песни для Death in Fire', 'Death in Fire', (SELECT id FROM bands WHERE name = 'Amon Amarth')),
    (nextval('song_sequence'), 320, E'Текст песни для The Way of Vikings', 'The Way of Vikings', (SELECT id FROM bands WHERE name = 'Amon Amarth')),
    (nextval('song_sequence'), 260, E'Текст песни для Raise Your Horns', 'Raise Your Horns', (SELECT id FROM bands WHERE name = 'Amon Amarth')),
    (nextval('song_sequence'), 300, E'Текст песни для Runes to My Memory', 'Runes to My Memory', (SELECT id FROM bands WHERE name = 'Amon Amarth')),
    (nextval('song_sequence'), 310, E'Текст песни для War of the Gods', 'War of the Gods', (SELECT id FROM bands WHERE name = 'Amon Amarth')),
    (nextval('song_sequence'), 270, E'Текст песни для The Pursuit of Oden', 'The Pursuit of Oden', (SELECT id FROM bands WHERE name = 'Amon Amarth')),
    (nextval('song_sequence'), 290, E'Текст песни для Twilight of the Gods', 'Twilight of the Gods', (SELECT id FROM bands WHERE name = 'Amon Amarth'));