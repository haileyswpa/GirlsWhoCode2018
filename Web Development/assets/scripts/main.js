var heroes = [
    {
        name: "D.Va",
        location: 'Busan, South Korea',
        quote: 'I PLAY TO WIN.',
        bio: 'D.Va is a former professional gamer who now uses her skills to pilot a state-of-the-art mech in defense of her homeland.',
        role: 'Tank',
        image: 'https://d1u1mce87gyfbn.cloudfront.net/hero/dva/hero-select-portrait.png',
        color: '#f825c2'
    },
    {
        name: 'Orisa',
        location: 'Numbani',
        quote: 'YOUR SAFETY IS MY PRIMARY CONCERN.',
        bio: 'Built from parts of one of Numbani\'s short-lived OR15 defense robots, Orisa is the city\'s newest protector, though she still has much to learn.',
        role: 'Tank',
        image: 'https://d1u1mce87gyfbn.cloudfront.net/hero/orisa/hero-select-portrait.png',
        color: '#758817'
    },
    {
        name: 'Reinhardt',
        location: 'Stuttgart, Germany',
        quote: 'JUSTICE WILL BE DONE.',
        bio: 'Reinhardt Wilhelm styles himself as a champion of a bygone age, who lives by the knightly codes of valor, justice, and courage.',
        role: 'Tank',
        image: 'https://d1u1mce87gyfbn.cloudfront.net/hero/reinhardt/hero-select-portrait.png',
        color: '#96695d'
    },
    {
        name: 'Roadhog',
        location: 'Junkertown, Australia',
        quote: 'I\'M A ONE-MAN APOCALYPSE.',
        bio: 'Roadhog is a ruthless killer with a well-earned reputation for cruelty and wanton destruction.',
        role: 'Tank',
        image: 'https://d1u1mce87gyfbn.cloudfront.net/hero/roadhog/hero-select-portrait.png',
        color: '#f4bc00'
    },
    {
        name: 'Winston',
        location: 'Horizon Lunar Colony',
        quote: 'IMAGINATION IS THE ESSENCE OF DISCOVERY.',
        bio: 'A super-intelligent, genetically engineered gorilla, Winston is a brilliant scientist and a champion for humanity\'s potential.',
        role: 'Tank',
        image: 'https://d1u1mce87gyfbn.cloudfront.net/hero/winston/hero-select-portrait.png',
        color: '#28314a'
    },
    {
        name: 'Zarya',
        location: 'Krasnoyarsk Front, Russia',
        quote: 'TOGETHER WE ARE STRONG.',
        bio: 'Aleksandra Zaryanova is one of the world\'s strongest women, a celebrated athlete who sacrificed personal glory to protect her family, friends, and country in a time of war.',
        role: 'Tank',
        image: 'https://d1u1mce87gyfbn.cloudfront.net/hero/zarya/hero-select-portrait.png',
        color: '#f12a94'
    },
    {
        name: 'Bastion',
        location: 'Unknown',
        quote: '...',
        bio: 'Once a frontline combatant in the devastating Omnic Crisis, this curious Bastion unit now explores the world, fascinated by nature but wary of a fearful humanity.',
        role: 'Damage',
        image: 'https://d1u1mce87gyfbn.cloudfront.net/hero/bastion/hero-select-portrait.png',
        color: '#4d8426'
    },
    {
        name: 'DOOMFIST',
        location: 'Oyo, Nigeria',
        quote: 'ONLY THROUGH CONFLICT DO WE EVOLVE.',
        bio: 'Recently freed from imprisonment, Doomfist is determined to plunge the world into a new conflict that he believes will make humanity stronger.',
        role: 'Damage',
        image: 'https://d1u1mce87gyfbn.cloudfront.net/hero/doomfist/hero-select-portrait.png',
        color: '#c01417'
    },
    {
        name: 'Genji',
        location: 'Shambali Monastery, Nepal',
        quote: 'EVEN IF I SACRIFICE MY BODY, I WILL NEVER SACRIFICE MY HONOR.',
        bio: 'The cyborg Genji Shimada has made peace with the augmented body he once rejected, and in doing so, he has discovered a higher humanity.',
        role: 'Damage',
        image: 'https://d1u1mce87gyfbn.cloudfront.net/hero/genji/hero-select-portrait.png',
        color: '#7cdf1a'
    },
    {
        name: 'Hanzo',
        location: 'Hanamura, Japan',
        quote: 'WITH EVERY DEATH COMES HONOR. WITH HONOR, REDEMPTION.',
        bio: 'Mastering his skills as a bowman and an assassin, Hanzo Shimada strives to prove himself as a warrior without peer.',
        role: 'Damage',
        image: 'https://d1u1mce87gyfbn.cloudfront.net/hero/hanzo/hero-select-portrait.png',
        color: '#183e6c'
    },
    {
        name: 'Junkrat',
        location: 'Junkertown, Australia',
        quote: 'IT\'S A PERFECT DAY FOR SOME MAYHEM.',
        bio: 'Junkrat is an explosives-obsessed freak who lives to cause chaos and destruction.',
        role: 'Damage',
        image: 'https://d1u1mce87gyfbn.cloudfront.net/hero/junkrat/hero-select-portrait.png',
        color: '#b0740d'
    },
    {
        name: 'McCree',
        location: 'Santa Fe, New Mexico, USA',
        quote: 'JUSTICE AIN\'T GONNA DISPENSE ITSELF.',
        bio: 'Armed with his Peacekeeper revolver, the outlaw Jesse McCree doles out justice on his own terms.',
        role: 'Damage',
        image: 'https://d1u1mce87gyfbn.cloudfront.net/hero/mccree/hero-select-portrait.png',
        color: '#811f1f'
    },
    {
        name: 'Mei',
        location: 'Xi\'an, China',
        quote: 'OUR WORLD IS WORTH FIGHTING FOR.',
        bio: 'Mei is a scientist who has taken the fight to preserve the environment into her own hands.',
        role: 'Damage',
        image: 'https://d1u1mce87gyfbn.cloudfront.net/hero/mei/hero-select-portrait.png',
        color: '#5dd0f3'
    },
    {
        name: 'PHARAH',
        location: 'Giza, Egypt',
        quote: 'I WILL PROTECT THE INNOCENT.',
        bio: 'Fareeha Amari\'s commitment to duty runs in her blood. She comes from a long line of highly decorated soldiers and burns with the desire to serve with honor.',
        role: 'Damage',
        image: 'https://d1u1mce87gyfbn.cloudfront.net/hero/pharah/hero-select-portrait.png',
        color: '#1562c6'
    },
    {
        name: 'REAPER',
        location: 'Unknown',
        quote: 'DEATH WALKS AMONG YOU.',
        bio: 'Some speak of a black-robed terrorist known only as the Reaper. His identity and motives are a mystery. What is known is that where he appears, death follows.',
        role: 'Damage',
        image: 'https://d1u1mce87gyfbn.cloudfront.net/hero/reaper/hero-select-portrait.png',
        color: '#16111a'
    },
    {
        name: 'SOLDIER: 76',
        location: 'Unknown',
        quote: 'WE\'RE ALL SOLDIERS NOW."',
        bio: 'Currently the target of an international manhunt, the vigilante known as Soldier: 76 wages a personal war to expose the truth behind Overwatch\'s collapse.',
        role: 'Damage',
        image: 'https://d1u1mce87gyfbn.cloudfront.net/hero/soldier-76/hero-select-portrait.png',
        color: '#2d55af'
    },
    {
        name: 'Sombra',
        location: 'Dorado, Mexico',
        quote: 'EVERYTHING CAN BE HACKED... AND EVERYONE.',
        bio: 'One of the world\'s most notorious hackers, Sombra uses information to manipulate those in power.',
        role: 'Damage',
        image: 'https://d1u1mce87gyfbn.cloudfront.net/hero/sombra/hero-select-portrait.png',
        color: '#6d08ff'
    },
    {
        name: 'SYMMETRA',
        location: 'Utopaea, India',
        quote: 'THE TRUE ENEMY OF HUMANITY IS DISORDER.',
        bio: 'Symmetra literally bends reality. By manipulating hard-light constructs, she crafts the world as she wishes it to be, in hopes of engineering a perfect society.',
        role: 'Damage',
        image: 'https://d1u1mce87gyfbn.cloudfront.net/hero/symmetra/hero-select-portrait.png',
        color: '#2eebf4'
    },
    {
        name: 'TORBJORN',
        location: 'Gothenburg, Sweden',
        quote: 'BUILD \'EM UP, BREAK \'EM DOWN.',
        bio: 'At its height, Overwatch possessed one of the most advanced armaments on the planet, which could be traced to the workshop of an ingenious engineer named Torbjorn Lindholm.',
        role: 'Damage',
        image: 'https://d1u1mce87gyfbn.cloudfront.net/hero/torbjorn/hero-select-portrait.png',
        color: '#6e1310'
    },
    {
        name: 'TRACER',
        location: 'London, England',
        quote: 'CHEERS, LOVE! THE CAVALRY\'S HERE!',
        bio: 'The former Overwatch agent known as Tracer is a time-jumping adventurer and an irrepressible force for good.',
        role: 'Damage',
        image: 'https://d1u1mce87gyfbn.cloudfront.net/hero/tracer/hero-select-portrait.png',
        color: '#e87400'
    },
    {
        name: 'WIDOWMAKER',
        location: 'Annecy, France',
        quote: 'ONE SHOT, ONE KILL.',
        bio: 'Widowmaker is the perfect assassin: a patient, ruthlessly efficient killer who shows neither emotion nor remorse.',
        role: 'Damage',
        image: 'https://d1u1mce87gyfbn.cloudfront.net/hero/widowmaker/hero-select-portrait.png',
        color: '#3a41af'
    },
    {
        name: 'ANA',
        location: 'Cairo, Egypt',
        quote: 'EVERYONE MUST FIND THEIR CAUSE.',
        bio: 'One of the founding members of Overwatch, Ana uses her skills and expertise to defend her home and the people she cares for.',
        role: 'Support',
        image: 'https://d1u1mce87gyfbn.cloudfront.net/hero/ana/hero-select-portrait.png',
        color: '#bba27a'
    },
    {
        name: 'BRIGITTE',
        location: 'Gothenburg, Sweden',
        quote: 'I WILL PROVE MYSELF!',
        bio: 'No longer sitting on the sidelines, Brigitte Lindholm has taken up arms to defend those in need of protection.',
        role: 'Support',
        image: 'https://d1u1mce87gyfbn.cloudfront.net/hero/brigitte/hero-select-portrait.png',
        color: '#531411'
    },
    {
        name: 'LUCIO',
        location: 'Rio de Janeiro, Brazil',
        quote: 'COME ON, LET\'S BRING IT TOGETHER!',
        bio: 'Lucio is an international celebrity who inspires social change through his music and actions.',
        role: 'Support',
        image: 'https://d1u1mce87gyfbn.cloudfront.net/hero/lucio/hero-select-portrait.png',
        color: '#8fc014'
    },
    {
        name: 'MERCY',
        location: 'Zürich, Switzerland',
        quote: 'HEROES NEVER DIE.',
        bio: 'A guardian angel to those who come under her care, Dr. Angela Ziegler is a peerless healer, a brilliant scientist, and a staunch advocate for peace.',
        role: 'Support',
        image: 'https://d1u1mce87gyfbn.cloudfront.net/hero/mercy/hero-select-portrait.png',
        color: '#f9bc15'
    },
    {
        name: 'MOIRA',
        location: 'Dublin, Ireland',
        quote: 'SCIENCE WILL REVEAL THE TRUTH.',
        bio: 'Equal parts brilliant and controversial, scientist Moira O\'Deorain is on the cutting edge of genetic engineering, searching for a way to rewrite the fundamental building blocks of life.',
        role: 'Support',
        image: 'https://d1u1mce87gyfbn.cloudfront.net/hero/moira/hero-select-portrait.png',
        color: '#3f03ae'
    },
    {
        name: 'ZENYATTA',
        location: 'Shambali Monastery, Nepal',
        quote: 'TRUE SELF IS WITHOUT FORM.',
        bio: 'Zenyatta is an omnic monk who wanders the world in search of spiritual enlightenment. It is said that those who cross his path are never the same again.',
        role: 'Support',
        image: 'https://d1u1mce87gyfbn.cloudfront.net/hero/zenyatta/hero-select-portrait.png',
        color: '#a57a0c'
    }
];
