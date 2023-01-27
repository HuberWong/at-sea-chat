//
//  ViewController.m
//  ASeaChat-frontend-iOS-OC
//
//  Created by huber wang on 2023/1/22.
//

#import "ViewController.h"
#import "AFNetworking.h"
@interface ViewController ()

@property(nonatomic, strong, readwrite)UILabel *label;

@end

@implementation ViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    // Do any additional setup after loading the view.
    self.title = @"ViewController";
    self.view.backgroundColor = [UIColor whiteColor];
    
    
    self.label = [[UILabel alloc] initWithFrame: CGRectMake(20, 140, self.view.frame.size.width, 40)];
    self.label.text = @"needed to be loaded";
    [self.view addSubview:self.label];
    
    
    UIButton *button = [UIButton buttonWithType:UIButtonTypeSystem];
    button.frame = CGRectMake(20, 100, 80, 40);
    [button setTitle:@"确定" forState:UIControlStateNormal];
    [button addTarget:self action:@selector(_hw2Label) forControlEvents:UIControlEventTouchUpInside];
    
    
    [self.view addSubview:button];
    
}

-(void)_hw2Label {
    NSString *URLString = @"http:192.168.2.2:8000";
    NSDictionary *parameters = @{};
    
    AFHTTPSessionManager *manager = [AFHTTPSessionManager manager];
    manager.responseSerializer = [AFHTTPResponseSerializer serializer];
    
    [manager GET:URLString parameters:parameters headers:nil progress:nil success:^(NSURLSessionDataTask * _Nonnull task, id  _Nullable responseObject) {
        NSDictionary *a = [NSJSONSerialization JSONObjectWithData:responseObject options:NSJSONReadingMutableLeaves error:nil];
        self.label.text = (NSString *)[a objectForKey:@"message"];
        
    } failure:^(NSURLSessionDataTask * _Nullable task, NSError * _Nonnull error) {
        NSLog(@"failure");
    }];
}


@end
