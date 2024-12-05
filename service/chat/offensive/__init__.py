import re

# The idea of this list is to filter the most extreme and most common ways to
# offend in intros. Because it only applies to intros, we've aimed for broad
# terms that could be acceptable in an *established* conversations, but are
# typically socially unacceptable at the start of a conversation.
#
# Although the list is likely to change over time, it probably won't change
# very frequently, so we'll just hardcode it rather than storing it in the DB.


_strings = [
    "anal",
    "anally",
    "anus",
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
    "ballsack",
    "beastial",
    "beastiality",
    "bellend",
    "bestiality",
    "bitch",
    "blow job",
    "blow jobs",
    "blowjob",
    "blowjobs",
    "breasts",
    "bukkake",
    "butt fuck",
    "butt fucked",
    "butt fucker",
    "butt fucking",
    "butt-fuck",
    "butt-fucked",
    "butt-fucker",
    "butt-fucking",
    "c0ck",
    "c0cksucker",
    "carpet muncher",
    "cawk",
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
    "coon",
    "coprophilia",
    "cum",
    "cumming",
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
    "dildo",
    "dildos",
    "dog-fucker",
    "doggin",
    "dogging",
    "dyke",
    "dykes",
    "e sex",
    "e-sex",
    "edging",
    "ejaculate",
    "ejaculated",
    "ejaculates",
    "ejaculating",
    "ejaculatings",
    "ejaculation",
    "ejakulate",
    "esex",
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
    "fuck yourself",
    "gang bang",
    "gangbang",
    "gangbanged",
    "gangbangs",
    "gaysex",
    "goatse",
    "golden shower",
    "gook",
    "gooks",
    "hang myself",
    "hang yourself",
    "hanged myself",
    "hanged yourself",
    "hanging myself",
    "hanging yourself",
    "horniest",
    "horny",
    "hotsex",
    "incest",
    "jack-off",
    "jackoff",
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
    "kill myself",
    "kill yourself",
    "killed myself",
    "killed yourself",
    "killing myself",
    "killing yourself",
    "kms",
    "kys",
    "labia",
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
    "necrophilia",
    "nigger",
    "niggers",
    "nigs",
    "nutsack",
    "orgasim",
    "orgasims",
    "orgasm",
    "orgasms",
    "orgy",
    "p0rn",
    "paedo",
    "paedophile",
    "paraphilias",
    "pedo",
    "pedophile",
    "pedophilia",
    "pegging",
    "penis",
    "penisfucker",
    "phonesex",
    "pissflaps",
    "pissin",
    "pissing",
    "porn",
    "porno",
    "pornography",
    "pornos",
    "prostitute",
    "pussies",
    "pussy",
    "pussys",
    "rape",
    "raped",
    "rapes",
    "raping",
    "rimjob",
    "rimming",
    "scrote",
    "scrotum",
    "semen",
    "sex",
    "shag",
    "shagging",
    "shemale",
    "shitdick",
    "shitfuck",
    "shota",
    "shotacon",
    "skank",
    "slut",
    "sluts",
    "smegma",
    "spic",
    "suicidal",
    "suicide",
    "testicle",
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
    "vagina",
    "viagra",
    "vulva",
    "wank",
    "wanker",
    "whore",
    "whores",
    "wincest",
    "you will never be a woman",
    "you'll never be a woman",
    "ywnbaw",
    "zoophilia",
]

for s in _strings:
    if not re.match("""^[-a-z0-9' ]+$""", s):
        raise AssertionError(s)

_pattern = '|'.join(f'(\\b{s}\\b)' for s in _strings)

_matcher = re.compile(_pattern, re.IGNORECASE)

def is_offensive(s: str) -> bool:
    normalized_input = ' '.join(s.split())

    return bool(_matcher.search(normalized_input))
