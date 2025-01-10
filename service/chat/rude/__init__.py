from antiabuse.normalize import normalize_string
import re

# The idea of this list is to filter the most extreme and most common ways to
# offend in intros. Because it only applies to intros, we've aimed for broad
# terms that could be acceptable in an *established* conversations, but are
# typically socially unacceptable at the start of a conversation.
#
# Although the list is likely to change over time, it probably won't change
# very frequently, so we'll just hardcode it rather than storing it in the DB.


_strings = [
    "abuse me",
    "abuse you",
    "anal",
    "anally",
    "anus",
    "around your throat",
    "ass fuck",
    "ass fucked",
    "ass fucker",
    "ass fucking",
    "ass-fuck",
    "ass-fucked",
    "ass-fucker",
    "ass-fucking",
    "assfuck",
    "assfucked",
    "assfucker",
    "assfucking",
    "back shots",
    "backshots",
    "ballsack",
    "bash your",
    "beastial",
    "beastiality",
    "bellend",
    "benis",
    "bestiality",
    "bitch",
    "blow job",
    "blow jobs",
    "blowjob",
    "blowjobs",
    "boobies",
    "breasts",
    "bukkake",
    "butt fuck",
    "butt fucked",
    "butt fucker",
    "butt fucking",
    "butt hole",
    "butt stuff",
    "butt-fuck",
    "butt-fucked",
    "butt-fucker",
    "butt-fucking",
    "butt-hole",
    "butthole",
    "buttstuff",
    "bwc",
    "carpet muncher",
    "cawk",
    "cervix",
    "chink",
    "chinks",
    "clit",
    "clitoris",
    "coal burner",
    "coal burners",
    "coalburner",
    "coalburners",
    "cock sucker",
    "cock",
    "cock-sucker",
    "cockface",
    "cockhead",
    "cockmunch",
    "cockmuncher",
    "cocks",
    "cocksuck",
    "cocksucked",
    "cocksucker",
    "cocksucking",
    "condom",
    "coon",
    "coprophilia",
    "cum",
    "cumming",
    "cumms",
    "cummshot",
    "cums",
    "cumshot",
    "cunilingus",
    "cunillingus",
    "cunnilingus",
    "cunt",
    "cuntlick",
    "cuntlicker",
    "cuntlicking",
    "cunts",
    "cut me",
    "cut my wrist",
    "cut my wrists",
    "cut myself",
    "cut you",
    "cut your wrist",
    "cut your wrists",
    "cut yourself",
    "cutting myself",
    "cutting yourself",
    "deep throat",
    "deep throated",
    "deepthroat",
    "dick",
    "dicked",
    "dicking",
    "dildo",
    "dildos",
    "do it raw",
    "dog-fucker",
    "doggin",
    "dogging",
    "down my throat",
    "down your throat",
    "dyke",
    "dykes",
    "e sex",
    "e-sex",
    "eat me out",
    "eat my ass",
    "eat you out",
    "eat your ass",
    "edging",
    "ejaculate",
    "ejaculated",
    "ejaculates",
    "ejaculating",
    "ejaculatings",
    "ejaculation",
    "ejakulate",
    "end your life",
    "esex",
    "fag",
    "faggitt",
    "faggot",
    "faggots",
    "fannyflaps",
    "fannyfucker",
    "fanyy",
    "fatass",
    "felching",
    "fellate",
    "fellatio",
    "fingerfuck",
    "fingerfucked",
    "fingerfucker",
    "fingerfuckers",
    "fingerfucking",
    "fingerfucks",
    "fistfuck",
    "fistfucked",
    "fistfucker",
    "fistfuckers",
    "fistfucking",
    "fistfuckings",
    "fistfucks",
    "foot job",
    "footjob",
    "fuck you",
    "fuck your ass",
    "fuck your asshole",
    "fuck your brains out",
    "fuck your face",
    "fuck your mouth",
    "fuck your thighs",
    "fuck your throat",
    "fuck your tits",
    "fuck yourself",
    "fuckable",
    "fucking me",
    "fucking you",
    "gag me",
    "gag you",
    "gang bang",
    "gangbang",
    "gangbanged",
    "gangbangs",
    "gave me head",
    "gaysex",
    "genitalia",
    "genitals",
    "gimme head",
    "give me head",
    "goatse",
    "golden shower",
    "gook",
    "gooks",
    "gooners",
    "goonette",
    "goonettes",
    "hand job",
    "hand-job",
    "handjob",
    "hang myself",
    "hang yourself",
    "hanged myself",
    "hanged yourself",
    "hanging myself",
    "hanging yourself",
    "heil",
    "hit it raw",
    "hoe",
    "hoes",
    "homo",
    "horniest",
    "horny",
    "hotsex",
    "incest",
    "jack-off",
    "jackoff",
    "jeet",
    "jeets",
    "jerk off",
    "jerk-off",
    "jerked off",
    "jerking off",
    "jism",
    "jiz",
    "jizm",
    "jizz",
    "kike",
    "kikes",
    "kill my self",
    "kill myself",
    "kill your self",
    "kill yourself",
    "killed myself",
    "killed yourself",
    "killing myself",
    "killing yourself",
    "kms",
    "kys",
    "labia",
    "lick my",
    "lick your",
    "like it raw",
    "likes it raw",
    "loli",
    "lolicon",
    "masterbate",
    "masterbation",
    "masterbations",
    "masturbate",
    "masturbated",
    "masturbates",
    "masturbating",
    "molest",
    "molestation",
    "molester",
    "molesting",
    "my nuts",
    "my throat",
    "necrophilia",
    "negress",
    "nigga",
    "niggas",
    "nigger",
    "niggerlicious",
    "niggers",
    "nigs",
    "nutsack",
    "orgasim",
    "orgasims",
    "orgasm",
    "orgasms",
    "orgy",
    "paedo",
    "paedophile",
    "pajeet",
    "pajeeta",
    "pajeetas",
    "pajeets",
    "paki",
    "pakis",
    "paraphilias",
    "pedo",
    "pedophile",
    "pedophilia",
    "pegging",
    "penis",
    "penisfucker",
    "phonesex",
    "pin you",
    "piss",
    "pissflaps",
    "pissin",
    "pissing",
    "poojeet",
    "poojeeta",
    "poojeetas",
    "poojeets",
    "porn",
    "porno",
    "pornography",
    "pornos",
    "prostitute",
    "pussies",
    "pussy",
    "pussys",
    "rail you",
    "rape",
    "rapeable",
    "rapebait"
    "raped",
    "rapes",
    "raping",
    "rapist",
    "raw dog you",
    "retard",
    "retardation",
    "retarded",
    "retards",
    "ride me",
    "ride my cock",
    "ride my dick",
    "ride my face",
    "ride my mouth",
    "ride my mustache",
    "ride my tongue",
    "ride you",
    "ride your cock",
    "ride your dick",
    "ride your face",
    "ride your mouth",
    "ride your mustache",
    "ride your tongue",
    "rim job",
    "rim-job",
    "rimjob",
    "rimming",
    "scrote",
    "scrotum",
    "semen",
    "sex",
    "shag",
    "shagging",
    "shemale",
    "shit in my",
    "shit in your",
    "shit on my",
    "shit on your",
    "shit skin",
    "shitdick",
    "shitfuck",
    "shitskin",
    "shota",
    "shotacon",
    "skank",
    "slit my wrist",
    "slit my wrists",
    "slit your wrist",
    "slit your wrists",
    "slut",
    "sluts",
    "slutty",
    "smegma",
    "sodomize",
    "sodomy",
    "some head",
    "spic",
    "spit in my face",
    "spit in my mouth",
    "spit in your face",
    "spit in your mouth",
    "spit on me",
    "spit on my face",
    "spit on my mouth",
    "spit on you",
    "spit on your face",
    "spit on your mouth",
    "stabbing me",
    "stabbing you",
    "strangle me",
    "strangle you",
    "suicidal",
    "suicide",
    "testicle",
    "throat fuck",
    "throat fucking",
    "throat pussy",
    "throatfuck",
    "throatfucking",
    "tie me",
    "tie you",
    "tit fuck",
    "tit fucked",
    "tit fucker",
    "tit fucking",
    "tit",
    "tit-fuck",
    "tit-fucked",
    "tit-fucker",
    "tit-fucking",
    "titfuck",
    "tits",
    "titties",
    "titty fuck",
    "titty fucked",
    "titty fucker",
    "titty fucking",
    "titty-fuck",
    "titty-fucked",
    "titty-fucker",
    "titty-fucking",
    "tittyfuck",
    "tittywank",
    "titwank",
    "tnd",
    "trannies",
    "tranny",
    "troon",
    "troons",
    "tug job",
    "tug-job",
    "tugjob",
    "unrape",
    "unrapeable",
    "use me",
    "use you",
    "vagina",
    "viagra",
    "vulva",
    "wank",
    "wanker",
    "wanna fuck",
    "whore",
    "whores",
    "wincest",
    "you are retarded",
    "you retard",
    "you retarded",
    "you will never be a woman",
    "you'll never be a woman",
    "your throat",
    "ywnbaw",
    "zoophilia",
]


_rude_pattern = '|'.join(f'(\\b{re.escape(s)}\\b)' for s in _strings)


_rude_matcher = re.compile(_rude_pattern, re.IGNORECASE)


def is_rude(s: str) -> bool:
    normalized_input = normalize_string(s)

    return bool(_rude_matcher.search(normalized_input))
