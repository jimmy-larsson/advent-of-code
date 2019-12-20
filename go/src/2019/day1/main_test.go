package main

import "testing"

func Test_part1(t *testing.T) {
	type args struct {
		inputOverride []int
		filepath      string
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		{
			name: "Single mass to fuel calculation",
			args: args{
				inputOverride: []int{100756},
				filepath:      "",
			},
			want: 33583,
		},
		{
			name: "Multiple mass to fuel calculations properly calculated and summed",
			args: args{
				inputOverride: []int{12, 14, 1969, 100756},
				filepath:      "",
			},
			want: 34241,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := part1(tt.args.inputOverride, tt.args.filepath); got != tt.want {
				t.Errorf("part1() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_part2(t *testing.T) {
	type args struct {
		inputOverride []int
		filepath      string
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		{
			name: "Testing single mass to recursed fuel calculation",
			args: args{
				inputOverride: []int{100756},
				filepath:      "",
			},
			want: 50346,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := part2(tt.args.inputOverride, tt.args.filepath); got != tt.want {
				t.Errorf("part2() = %v, want %v", got, tt.want)
			}
		})
	}
}
