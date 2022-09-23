export enum ImageStyle {
    MYSTICAL = 1,
    CYBER_PUNK = 2,
    VIBRANT = 3,
    DARK_FANTASY = 4,
    FANTASY = 5,
    TOWER = 6,
    RUNES = 7,
    SHAPE = 8
}

export interface GenerateImageStyleRequestBody {
    user_prompt: string
    image_style: number
}