ALIEN_HIVEMIND_CHARACTERS = """
{
    characters(filter: { species: "Alien", type: "Hivemind" }) {
        results {
            id
            name
            status
            species
            type
            gender
            image
            created
        }
    }
}
"""

DEAD_ASD_NO_RESULTS_CHARACTERS = """
{
    characters(filter: { type: "asd", status: "Dead" }) {
        results {
            id
            name
            status
            species
            type
            gender
            image
            created
        }
    }
}
"""

ID_NAME_SPECIES_GENDER_1_CHARACTER = """
{
    character(id: "1") {
        id
        name
        species
        gender
    }
}
"""
